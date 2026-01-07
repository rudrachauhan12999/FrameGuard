import cv2
import subprocess
import os
import imageio_ffmpeg


def extract_frames(video_path, max_frames=30):
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0

    while cap.isOpened() and count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame)
        count += 1

    cap.release()
    return frames


def extract_audio(video_path, output_audio="audio.wav"):
    print("Starting audio extraction with FFmpeg...")

    try:
        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

        cmd = [
            ffmpeg_path,
            "-y",
            "-i", video_path,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "44100",
            "-ac", "1",
            output_audio
        ]

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        if os.path.exists(output_audio):
            print("Audio written to file.")
            return output_audio
        else:
            print("FFmpeg ran but audio file not found.")
            return None

    except Exception as e:
        print("Audio extraction failed:", e)
        return None
