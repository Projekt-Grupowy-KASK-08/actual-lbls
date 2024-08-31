import time

import pandas as pd


def csv_data_stream(filepath, sampling_rate, chunk_size):
    """
    Generator that yields data from a CSV file based on the sampling rate.

    :param filepath: Path to the CSV file
    :param sampling_rate: Sampling rate (Hz)
    :param chunk_size: Number of samples to yield per update
    :return: A generator yielding y-values in chunks
    """
    df = pd.read_csv(filepath)
    raw_col = df['2: preprocessed'].values

    index = 0
    last_time = time.time()

    def generator():
        nonlocal index, last_time
        while True:
            current_time = time.time()
            time_since_last_sample = current_time - last_time
            if time_since_last_sample >= (1 / sampling_rate):
                if index < len(raw_col):
                    last_time = current_time
                    # Return a chunk of data
                    chunk = raw_col[index:index + chunk_size]
                    index += chunk_size
                    yield chunk
                else:
                    pass
                    # Restart from the beginning if all data is read
                    #index = 0
                    #last_time = time.time()

    return generator()