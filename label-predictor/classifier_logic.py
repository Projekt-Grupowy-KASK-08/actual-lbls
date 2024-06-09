import numpy as np


# Getting only the longest range
def get_longest_range(ranges):
    max_diff = 0
    start = 0
    end = 0
    for i in range(len(ranges['end_time'])):
        diff = ranges['end_time'][i] - ranges['start_time'][i]
        if diff > max_diff:
            max_diff = diff
            start = ranges['start_time'][i]
            end = ranges['end_time'][i]
    return start, end


# Calculating treashold based on neighbouring segments
def calculate_treshold(data, segment, segment_size, i):
    left_neighbour_segment = 10
    right_neighbour_segment = 10
    if i < left_neighbour_segment:
        left_neighbour_segment = i
    elif i + right_neighbour_segment > len(segment):
        right_neighbour_segment = len(segment) - i

    threshold = 7 * np.std(
        data.iloc[(i - left_neighbour_segment) * segment_size:(i + 1 + right_neighbour_segment) * segment_size][
            "2: preprocessed"])
    return threshold


def classify(data, segment_size):
    ranges = {
        'start_time': [],
        'end_time': []
    }

    segments = int(len(data) / segment_size)
    previous_was_accepted = False
    last_end_time = 0
    for i in range(segments):

        segment_start = i * segment_size
        segment_end = (i + 1) * segment_size
        if segment_end > len(data):
            segment_end = len(data)

        segment = data.iloc[segment_start:segment_end]
        threshold = calculate_treshold(data, segment, segment_size, i)
        extreme_spikes = np.where(segment["2: preprocessed"] > threshold)[0]
        zero_count = np.sum((segment["2: preprocessed"] >= -3) & (segment["2: preprocessed"] <= 3))

        if len(extreme_spikes) == 0 and zero_count / len(segment) < 0.6:
            if not previous_was_accepted:
                ranges['start_time'].append(segment['Time'].iloc[0])
            last_end_time = segment['Time'].iloc[-1]
            previous_was_accepted = True
        else:
            if previous_was_accepted:
                ranges['end_time'].append(last_end_time)
            previous_was_accepted = False

    if previous_was_accepted:
        ranges['end_time'].append(last_end_time)

    start, end = get_longest_range(ranges)
    return start, end
