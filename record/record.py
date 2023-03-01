import pyaudio
import wave

# Set the parameters for the audio recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

# Create an instance of the PyAudio class
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

print("Recording...")

# Record audio for 5 seconds
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the audio recording to a WAV file
filename = "recording.wav"
wf = wave.open(filename, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()

print(f"Saved recording to {filename}")
