# Gender Prediction Using XGBoost

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [License](#license)
- [Contact](#contact)

## Overview

This project implements a machine learning model to predict gender based on voice features using the XGBoost classifier. The system includes components for recording and processing audio data, extracting features, and predicting gender with high accuracy. It provides tools for GUI interactions, QR code generation, and more, offering a comprehensive solution for voice-based gender prediction.

## Features

- **Voice Feature Extraction**: Extracts key acoustic features from audio files for use in gender prediction.
- **Voice Recording**: Captures audio data using a microphone and saves it as a WAV file.
- **Gender Prediction**: Utilizes an XGBoost classifier to predict gender based on extracted voice features.
- **GUI Tools**: Provides various GUI components, including a custom spinbox, modern windows, and a countdown timer.
- **QR Code Generation**: Generates and saves QR codes based on input data.
- **Secret Code Generation**: Creates a 48-character alphanumeric secret code.

## Requirements

Ensure that the following Python packages are installed:

- Python 3.6 or higher
- `scipy`
- `librosa`
- `pydub`
- `pyaudio`
- `xgboost`
- `sklearn`
- `pandas`
- `tkinter`
- `customtkinter`
- `qrcode`
- `secrets`

## Installation

 **Install Dependencies**

   ```bash
   pip install scipy librosa pydub pyaudio xgboost scikit-learn pandas customtkinter qrcode secrets
   ```

## Usage

1. **Extract Acoustic Features**

   Use the `acausticfeatersextract.py` script to extract features from an audio file:

   ```python
   from acausticfeatersextract import extract_features
   features = extract_features("your_audio_file.mp3")
   ```

2. **Record Your Voice**

   Use the `recorder.py` script to record your voice:

   ```bash
   python recorder.py
   ```

   This will record your voice and save it as `recorded_voice.wav`.

3. **Train the Model**

   Run the `XGBmodel.py` script to train the XGBoost model on the `voice.csv` dataset:

   ```bash
   python XGBmodel.py
   ```

   The model will be trained, and you can use the `xgb_predict` function to make predictions.

4. **Make Predictions**

   After training, use the `xgb_predict` function to predict gender based on the extracted features:

   ```python
   from XGBmodel import xgb_predict
   prediction = xgb_predict(features)
   print(f"Predicted Gender: {prediction}")
   ```

## Code Structure

The project comprises the following key components:

1. **`acausticfeatersextract.py`**: Handles acoustic feature extraction from audio files.
2. **`recorder.py`**: Manages voice recording and file saving.
3. **`timer.py`**: Implements a countdown timer using customtkinter.
4. **`tools.py`**: Contains utility functions for QR code generation, secret code creation, and GUI components.
5. **`XGBmodel.py`**: Includes data preprocessing, model training, and gender prediction using XGBoost.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, feel free to contact [yacermeftah@gmail.com].
