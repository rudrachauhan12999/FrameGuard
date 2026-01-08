DEPLOY_MODE = True
print("WEB APP FILE EXECUTED")

from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# LOCAL-ONLY IMPORTS
# =========================
if not DEPLOY_MODE:
    from agents.scout_agent import extract_frames, extract_audio
    from agents.frame_selector_agent import select_key_frames
    from agents.audio_agent import analyze_audio
    from agents.vision_agent import analyze_frames
    from agents.decision_agent import fuse_scores
    from utils.report_generator import generate_report, generate_text_report


@app.route("/", methods=["GET", "POST"])
def index():

    # =========================
    # CLOUD / LITE MODE
    # =========================
    if DEPLOY_MODE:
        return jsonify({
            "service": "FrameGuard",
            "status": "live",
            "mode": "lite deployment",
            "note": "Heavy audio/video forensics disabled on free-tier cloud deployment"
        })

    # =========================
    # LOCAL / FULL MODE
    # =========================
    result = None

    if request.method == "POST":
        file = request.files["media"]
        filename = file.filename.lower()
        media_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(media_path)

        # VIDEO PIPELINE
        if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
            frames = extract_frames(media_path)
            audio_file = extract_audio(media_path)
            selected_frames = select_key_frames(frames)

            audio_score = analyze_audio(audio_file)
            visual_score = analyze_frames(selected_frames)

            total_frames = len(frames)
            selected_count = len(selected_frames)

        # IMAGE PIPELINE
        elif filename.endswith((".jpg", ".jpeg", ".png")):
            import cv2
            import numpy as np

            image = cv2.imread(media_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

            visual_score = max(0.0, min(1.0, 1.0 - (laplacian_var / 1500)))
            audio_score = 0.3  # uncertainty penalty for image-only input

            total_frames = 1
            selected_count = 1

        else:
            return "Unsupported file type", 400

        final_score, verdict = fuse_scores(audio_score, visual_score)

        report_data = {
            "video": file.filename,
            "total_frames": total_frames,
            "selected_frames": selected_count,
            "audio_score": audio_score,
            "visual_score": visual_score,
            "final_score": final_score,
            "verdict": verdict
        }

        generate_report(report_data)
        generate_text_report(report_data)

        result = {
            "verdict": verdict,
            "final_score": round(final_score, 3)
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)


