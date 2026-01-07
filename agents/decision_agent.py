def fuse_scores(audio_score, visual_score):
    print("Decision Agent: fusing scores...")

    final_score = (0.5 * audio_score) + (0.5 * visual_score)

    if final_score < 0.45:
        verdict = "LIKELY AUTHENTIC"
    elif final_score < 0.75:
        verdict = "INCONCLUSIVE – NEEDS REVIEW"
    else:
        verdict = "POTENTIAL DEEPFAKE"

    return final_score, verdict
