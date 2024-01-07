import scipy.stats as stats
import scipy.signal as signal
import numpy as np

def read_from_dat_file(filepath, encoding=np.int16, offset=0x0000025C):
    """Reads data from .dat file and  returns one dimensional numpy array"""
    return np.fromfile(filepath, dtype=encoding, offset=offset)

def bandpass_filter(data, frequency=20000, lowcut=500, highcut=5000, order=4):
    fs = frequency
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    order = 4
    
    b, a = signal.butter(order, [low, high], btype='band')
    y = signal.lfilter(b, a, data)
    
    return y

def artifact_removal(data, vc_threshold=1.8, segments=10000):
    clear_data = []
    last_variance = 1
    segment_length = int(len(data)/segments)
    
    for i in range(segments - 1):
        segment = data[i * segment_length:(i+1) * segment_length]

        variance = stats.variation(segment)
        if (variance/last_variance <= vc_threshold):
            clear_data.extend(segment)
        last_variance = variance

    return clear_data

def clip_data(data, minValue=-500, maxValue=500):
    clippedData = np.clip(data, minValue, maxValue)
    return clippedData

def remove_duplicates_from_list(x):
  return list(dict.fromkeys(x))

def preprocess_raw_data(data):
    data = artifact_removal(data)
    data = bandpass_filter(data)
    data = clip_data(data)
    return data