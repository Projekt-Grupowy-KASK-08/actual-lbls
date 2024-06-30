import pandas as pd
import wave
import struct
import os

# Base directory
base_dir = 'C:\\Users\\kasia\\OneDrive\\Pulpit\\pacjenci\\'

# Read the CSV file
df = pd.read_csv(base_dir + 'label_with_file_path.csv')
file_path = r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Wolf Krzysztof\546253247\depth-1,0_kanalCentral.csv"
csv = pd.read_csv(file_path)

signal = csv["2: preprocessed"]

print(f"Ilosc probek: {len(signal)}")

def scale_value(v : float) -> float:
    """Ensures that the value is in the range [-1, 1]"""
    v = v / 500.0
    v = max(-1.0, min(1.0, v))
    return v

# Uses variable signal from above

# Open up a wave file
name = os.path.basename(file_path)
output = wave.open(f"wav/{name}.wav", 'w')

# Set the parameters of the wave file
nchannels = 1
sampwidth = 2
framerate = 44100
nframes = len(signal)
comptype = "NONE"
compname = "not compressed"
output.setparams((
    nchannels,
    sampwidth,
    framerate,
    nframes,
    comptype,
    compname
))


# Write the audio frames to the wave file
for v in signal:
    v = scale_value(v)
    output.writeframes(struct.pack('h', int(v * 32767.0)))

# Close the wave file
output.close()
print("Done!")
