import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def analyze_audio(audio_path):
    print("Audio Agent: analyzing audio...")

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Generate spectrogram
    spectrogram = librosa.amplitude_to_db(
        np.abs(librosa.stft(y)),
        ref=np.max
    )

    # Plot spectrogram
    plt.figure(figsize=(8, 4))
    librosa.display.specshow(
        spectrogram,
        sr=sr,
        x_axis="time",
        y_axis="log"
    )
    plt.colorbar(format="%+2.0f dB")
    plt.title("Audio Spectrogram")
    plt.tight_layout()
    plt.savefig("audio_spectrogram.png")
    plt.close()

    # Dummy risk score (replace later)
    audio_risk_score = float(np.random.uniform(0.3, 0.9))

    print("Audio Agent: spectrogram saved.")
    return audio_risk_score

