import cv2
import numpy as np


def select_key_frames(frames, threshold=30):
    """
    Select frames with significant visual change
    """
    selected_frames = []
    prev_gray = None

    for idx, frame in enumerate(frames):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is None:
            selected_frames.append((idx, frame))
            prev_gray = gray
            continue

        diff = cv2.absdiff(prev_gray, gray)
        score = np.mean(diff)

        if score > threshold:
            selected_frames.append((idx, frame))
            prev_gray = gray

    return selected_frames
