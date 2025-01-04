import sounddevice as sd
import numpy as np
import wavio

# Audio constants
sample_rate = 44100  # Hz
record_duration = 10  # Seconds
filename =  input('Type recorder name: ')
output_filename = filename + ".wav"

# Record audio
print("Recording...")
channels = 1 # or two for dual channel
audio_data = sd.rec(int(sample_rate * record_duration), samplerate=sample_rate, channels=channels, dtype=np.int16)
sd.wait()

# Save the recorded audio to a WAV file
print("Saving recording to: ", output_filename)
wavio.write(output_filename, audio_data, sample_rate, sampwidth=2)

print("Recording saved as: ", output_filename)
