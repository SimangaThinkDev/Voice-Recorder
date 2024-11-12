Here's an example **README.md** for your voice recorder Python project that explains the purpose, dependencies, and how to use the code. It also provides instructions for installation and how to troubleshoot common issues.

---

# Voice Recorder in Python

## Overview

Welcome to the Python Voice Recorder project! This project allows you to record audio using your microphone and save it as a `.wav` file. The code utilizes the **PyAudio** library to capture audio data and store it into a file in real-time.

### Key Features:
- **Real-time Audio Recording**: Capture audio in real-time from your microphone.
- **Custom File Naming**: You can choose the name of your recorded file.
- **Error Handling**: Handles interruptions gracefully (e.g., when you stop recording using `Ctrl+C`).

---

## Prerequisites

To run this project, you'll need to install the following dependencies:

### Required Libraries:
- **PyAudio**: For audio input/output handling.
- **wave**: For saving the recorded audio to a `.wav` file.

You can install the dependencies using **pip**:

```bash
pip install pyaudio
```

**Note**: If you're on Windows, you may need to install the appropriate **PyAudio** wheel, as it can sometimes be tricky to install directly via pip. You can find precompiled wheels at: [PyAudio wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

---

## Setup & Usage

### Step 1: Clone the repository
First, clone or download this repository to your local machine:

```bash
git clone https://github.com/your-username/voice-recorder.git
cd voice-recorder
```

### Step 2: Run the script
Once the dependencies are installed, you can run the script to start recording audio. The code will run a continuous loop and save the recorded audio when you stop it.

```bash
python recorder.py
```

### Step 3: Name your recording
When you stop recording by pressing `Ctrl+C` (KeyboardInterrupt), you will be prompted to name your `.wav` file. Enter the desired name for the file (e.g., `my_recording.wav`), and the recording will be saved with that name.

Example:

```bash
What would you like to name your recording? my_recording.wav
```

### Step 4: Check the saved file
Once the script completes, you'll find the recorded audio file in the same directory as the script.

---

## How It Works

1. **Recording**: The script initializes a PyAudio stream, specifying the audio format (`pyaudio.paInt16`), sample rate (44100 Hz), and input device for recording. The script continuously captures audio data in chunks of 1024 frames.
2. **Interrupt Handling**: The `try` block is used to continuously record until a `KeyboardInterrupt` (when you press `Ctrl+C`). The program then gracefully stops and writes the captured audio data to a `.wav` file.
3. **Saving the File**: The audio data is saved using Python's `wave` module, and the file is named based on user input.

---

## Troubleshooting

### Common Errors

#### 1. **OSError: [Errno -9981] Input Overflowed**
This error occurs when the audio buffer overflows, meaning the program is trying to read more audio than it can process in real-time. You can try the following to resolve it:
- Increase the buffer size by modifying the `frames_per_buffer` parameter when opening the stream:
    ```python
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=2048)
    ```
- Reduce the complexity of the audio processing or perform it in smaller chunks.

#### 2. **ModuleNotFoundError: No module named 'pyaudio'**
If you get this error, you may not have installed **PyAudio**. Install it using pip:
```bash
pip install pyaudio
```

For Windows, if you're still having trouble, use the precompiled `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

#### 3. **Permission Errors (Linux/macOS)**
If you encounter permission errors when accessing the microphone, try running the script with elevated permissions:
```bash
sudo python recorder.py
```

---

## Contributing

Feel free to contribute by forking the repository, submitting issues, and creating pull requests.

If you have ideas for new features or improvements, don't hesitate to open an issue or start a discussion!

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgements

- **PyAudio**: For handling real-time audio input/output.
- **Wave**: For encoding and saving the recorded audio into `.wav` format.

---

### Example of script (`recorder.py`):

```python
import pyaudio
import wave

# Assign pyaudio object to a variable
audio = pyaudio.PyAudio()

# Create a stream to record our audio, encoded
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Store the recording in a list frames
frames = []

print("[STATUS:] Recording has Started")

# The reason for creating a try-catch is because we want to stop recording with a keyboard interrupt
try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    print("[STATUS:] Recording has stopped")
    pass

# Close the dependencies
stream.stop_stream()
stream.close()
audio.terminate()

# Decode frames and assign to var recording
recording = wave.open(f"{input('What would you like to name your recording? ')}.wav", "wb")

# Initialize recording to receive audio information
recording.setnchannels(1)
recording.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
recording.setframerate(44100)

# Assign audio information
recording.writeframes(b"".join(frames))
```

---

This README file should guide users through setting up and using the voice recorder script while offering solutions to common errors. Let me know if you need any more details!
