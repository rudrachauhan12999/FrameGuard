import numpy as np
import cv2


def analyze_frames(selected_frames):
    """
    Analyze selected frames for visual inconsistencies.
    Returns a visual risk score.
    """
    print("Vision Agent: analyzing selected frames...")

    scores = []

    for idx, frame in selected_frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Simple sharpness / noise proxy
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

        # Normalize into a fake risk score range
        score = np.clip(1.0 - (laplacian_var / 1000), 0.0, 1.0)
        scores.append(score)

    if not scores:
        return 0.0

    visual_risk_score = float(np.mean(scores))
    print("Vision Agent: visual risk score computed.")

    return visual_risk_score
