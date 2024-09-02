
import pyaudio
import wave

def list_input_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("Available input devices:")
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Device {} - {}".format(i, p.get_device_info_by_host_api_device_index(0, i).get('name')))

def record_voice(filename="recorded_voice.wav", input_device_index=0, duration=5, sample_rate=44100, chunk_size=1024):
    list_input_devices()
    p = pyaudio.PyAudio()

    # Open a stream with the specified input device
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    input_device_index=input_device_index,
                    frames_per_buffer=chunk_size)

    print("Recording...")

    frames = []
    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data to a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename

if __name__ == "__main__":
    list_input_devices()  # Uncomment to list available input devices
    input_device_index = 0  # Adjust the index based on your chosen input device

    file_name = "recorded_voice.wav"
    record_duration = 5  # in seconds

    record_voice(file_name, input_device_index, duration=record_duration)
    print(f"Voice recording saved as '{file_name}'")


