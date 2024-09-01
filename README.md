# Gender Prediction Using XGBoost

This project demonstrates the use of the XGBoost classifier to predict gender based on voice features. The model is trained on a dataset of voice recordings, and it predicts whether a given voice is male or female.

## Project Structure

- **`acausticfeatersextract.py`**: This script extracts various acoustic features from an audio file using libraries such as `librosa` and `pydub`. The features include spectral entropy, spectral flatness, spectral centroid, and others. These features can then be used as input to the machine learning model.

- **`recorder.py`**: This script allows you to record your voice using a microphone. It lists available input devices, records the voice, and saves the recording as a WAV file. This recorded file can be used to extract features for gender prediction.

- **`timer.py`**: A simple timer widget built using `customtkinter` and `tkinter`. It creates a graphical interface with a countdown timer that can be started and reset.

- **`tools.py`**: A collection of utility functions, including:
  - `CTkSpinbox`: A custom spinbox widget for selecting numeric values.
  - `modern_window` and `new_window`: Functions to create modern or classic GUI windows.
  - `Qrcode`: Function to generate and save a QR code image.
  - `generate_secret_code`: Function to generate a random secret code of 48 characters.

- **`XGBmodel.py`**: This script handles the main machine learning task:
  - Loads and preprocesses the `voice.csv` dataset.
  - Trains an XGBoost model to predict gender based on voice features.
  - Contains a `xgb_predict` function to make predictions on new data.

## Requirements

To run this project, you need the following Python packages:

- `scipy`
- `librosa`
- `pydub`
- `pyaudio`
- `xgboost`
- `sklearn`
- `pandas`
- `tkinter`
- `customtkinter`
- `secrets`

You can install the required packages using pip:

```bash
pip install scipy librosa pydub pyaudio xgboost scikit-learn pandas customtkinter secrets
```

## How to Use

### 1. Extract Acoustic Features
Use the `acausticfeatersextract.py` script to extract features from an audio file (in MP3 format):

```python
from acausticfeatersextract import extract_features

features = extract_features("your_audio_file.mp3")
```

### 2. Record Your Voice
Use the `recorder.py` script to record your voice:

```bash
python recorder.py
```
This will record your voice and save it as `recorded_voice.wav`.

### 3. Train the Model
The `XGBmodel.py` script trains an XGBoost classifier on the `voice.csv` dataset:

```python
python XGBmodel.py
```
The model will be trained, and predictions can be made using the `xgb_predict` function.

### 4. Make Predictions
Once the model is trained, you can use the `xgb_predict` function to predict gender based on voice features:

```python
from XGBmodel import xgb_predict

prediction = xgb_predict(features)
print(f"Predicted Gender: {prediction}")
```

### 5. GUI Components
You can also explore the GUI components provided in `timer.py` and `tools.py` for creating modern interfaces and additional tools like QR code generation and secret code creation.

## Notes

- Ensure your dataset is clean and properly preprocessed before feeding it into the model.
- Adjust the `input_device_index` in `recorder.py` based on the microphone you want to use for recording.

## License

This project is open-source and free to use under the MIT License.

