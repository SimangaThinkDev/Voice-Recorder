#Welcome to my code that implements a voice recorder in python

#refer to the readme file for information about dependancies

import pyaudio
import wave

#Assign pyaudio object to a variable
audio = pyaudio.PyAudio()

#create a stream to record our audio, encoded
stream = audio.open(format= pyaudio.paInt16, channels=1, rate  = 44100, input = True, frames_per_buffer= 1024)

#Store the recording in a list frames

frames = []

print("[STATUS:] Recording has Started")
#The reason for creating a try catch is because we want to be able to stop recording with a keyboard interrupt
try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    print("[STATUS:] Recording has stopped")
    pass

#since we are done recording let's close the dependancies

stream.stop_stream()
stream.close()
audio.terminate

#decode frames and assign to var recording
recording = wave.open(f"{input('What would you like to name your recording? ')}.wav", "wb") 

#Initialize recording to receive audio information
recording.setnchannels(1)
recording.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
recording.setframerate(44100)

#assign audio information
recording.writeframes(b"".join(frames))
