import numpy as np
import scipy.signal as signal
import scipy.stats as stats

MIN_ENCODED = -2 ** 15
MAX_ENCODED = 2 ** 15 - 1


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


def clip_data(data, minValue=-500, maxValue=500):
    clippedData = np.clip(data, minValue, maxValue)
    return clippedData


def remove_duplicates_from_list(x):
    return list(dict.fromkeys(x))


def transform_data(data, threshold=50000):
    data = data.astype('float32')
    for (idx, n) in enumerate(data):
        if idx != 0 and abs(n - data[idx - 1]) > threshold:
            if n > 0:
                diff = MAX_ENCODED - n
                data[idx] = MIN_ENCODED - diff
            else:
                diff = n - MIN_ENCODED
                data[idx] = MAX_ENCODED + diff
    return data


def preprocess_raw_data(data):
    data = bandpass_filter(data)
    data = clip_data(data)
    return data
