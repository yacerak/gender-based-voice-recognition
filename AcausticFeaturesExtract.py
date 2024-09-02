

from scipy.stats import entropy
from pydub import AudioSegment
import librosa
import pydub
from librosa import feature
from librosa.feature import spectral_centroid, tempogram
import scipy.stats
from scipy.stats import kurtosis, skew
import pandas as pd
import os
import numpy as np

def spectral_entropy(x, sr, n_fft=2048, hop_length=512, normalize=False):
    # Compute the mel spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y=x, sr=sr, n_fft=n_fft, hop_length=hop_length)

    # Convert amplitude to decibels
    mel_spectrogram_db = librosa.amplitude_to_db(mel_spectrogram, ref=np.max)

    # Normalize the mel spectrogram
    mel_spectrogram_db /= mel_spectrogram_db.sum(axis=-1, keepdims=True)

    # Compute entropy
    entropy_values = -np.matmul(entropy(mel_spectrogram_db.T, base=2).reshape(1, -1), mel_spectrogram_db)

    return np.mean(entropy_values)

def extract_features(audio_file):
    # Check if the file exists
    if not os.path.exists(audio_file):
        print(f"Error: The file {audio_file} does not exist.")
        return

    # Load the MP3 file
    audio = AudioSegment.from_file(audio_file, format="mp3")

    # Convert the audio to WAV format (temporarily)
    temp_wav_file = "temp.wav"
    audio.export(temp_wav_file, format="wav")

    # Load the WAV file using librosa
    y, sr = librosa.load(temp_wav_file, sr=None)

    # Extract features
    sp_ent = spectral_entropy(y, sr)
    sfm = feature.spectral_flatness(y=y).mean()
    mode_array = scipy.stats.mode(y).mode
    mod = mode_array[0] if isinstance(mode_array, np.ndarray) and len(mode_array) > 0 else 0
    centroid = feature.spectral_centroid(y=y, sr=sr).mean()
    meanfun = feature.spectral_centroid(y=y, sr=sr).mean()
    minfun = feature.spectral_centroid(y=y, sr=sr).min()
    maxfun = feature.spectral_centroid(y=y, sr=sr).max()
    meandom = feature.spectral_centroid(y=y, sr=sr).mean()
    mindom = feature.spectral_centroid(y=y, sr=sr).min()
    maxdom = feature.spectral_centroid(y=y, sr=sr).max()
    dfrange = maxdom - mindom
    modindx = tempogram(y=y, sr=sr).mean()

    # Additional features
    meanfreq = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=1))
    sd = np.std(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=1))
    median = np.median(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=1))
    q25, q75 = np.percentile(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=1), [25, 75])
    iqr = q75 - q25
    skewness = skew(y)
    kurt = kurtosis(y)

    features_df = pd.DataFrame({
        'meanfreq': meanfreq,
        'sd': sd,
        'median': median,
        'Q25': q25,
        'Q75': q75,
        'IQR': iqr,
        'skew': skewness,
        'kurt': kurt,
        'sp.ent': sp_ent,
        'sfm': sfm,
        'mode': mod,
        'centroid': centroid,
        'meanfun': meanfun,
        'minfun': minfun,
        'maxfun': maxfun,
        'meandom': meandom,
        'mindom': mindom,
        'maxdom': maxdom,
        'dfrange': dfrange,
        'modindx': modindx
        }, index=['sample'])

    # Print the features
    #print(features_df)

    return features_df
