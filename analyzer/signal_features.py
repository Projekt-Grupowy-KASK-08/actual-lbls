import numpy as np
from numpy.fft import fft


def countSpikes(data):
    threshold = 3 * np.std(data)

    above_threshold = data > threshold

    # Count spikes only at the start of each above-threshold sequence
    spikes = np.diff(above_threshold.astype(int)) == 1

    # Add 1 to the result to account for the first spike if it starts at index 0
    spike_count = np.sum(spikes) + (above_threshold.iloc[0] == True)

    spike_indices = np.where(spikes)[0] + 1  # +1 to correct the index shift due to np.diff
    return spike_count, spike_indices


"""
    Calculate the average frequency of spikes in the data.
    
    f = Number of spikes / time
"""


def average_frequency_of_spikes(data, f=20000):
    spike_count, _ = countSpikes(data)
    return (spike_count / len(data)) * f


"""

    Calculate the frequency factor of the data.
    
    Rf = Number of intervals between 33ms and 66ms / number of intervals
    
"""


def calculate_intervals(spike_indices, f=20000):
    # Calculate time intervals between spikes
    intervals = np.diff(spike_indices) / f * 1000  # Convert to milliseconds
    return intervals


def frequency_coefficient(intervals):
    # Count intervals in the range 33 < ti < 66
    valid_intervals = (intervals > 33) & (intervals < 66)
    N33_66 = np.sum(valid_intervals)
    N_total = len(intervals)

    if N_total == 0:
        return 0

    Rf = N33_66 / N_total
    return Rf


"""
    Launch rate
    Rb = Number of intervals shorter 33ms / number of intervals
"""


def launch_rate(intervals):
    valid_intervals = intervals < 33
    N0_33 = np.sum(valid_intervals)
    N_total = len(intervals)

    if N_total == 0:
        return 0

    Rb = N0_33 / N_total
    return Rb


"""
    Pause indicator
    PI = Number of intervals shorter than 50ms / number of intervals longer than 50ms
"""


def pause_indicator(intervals):
    shorter_than_50ms = np.sum(intervals < 50)
    longer_than_50ms = np.sum(intervals > 50)

    if longer_than_50ms == 0:
        return 0

    PI = shorter_than_50ms / longer_than_50ms
    return PI


"""
    Pause ratio
    PR = Sum of time of intervals shorter than 50ms / Sum of time of intervals longer than 50ms
"""


def pause_ratio(intervals):
    # Sum of time of intervals shorter than 50ms
    sum_short_intervals = np.sum(intervals[intervals < 50])

    # Sum of time of intervals longer than 50ms
    sum_long_intervals = np.sum(intervals[intervals >= 50])

    if sum_long_intervals == 0:
        return 0

    PR = sum_short_intervals / sum_long_intervals
    return PR


"""
    Modified Launch rate
    Rb = Number of intervals shorter than 10ms / number of intervals longer than 10ms
"""


def modified_launch_rate(intervals):
    shorter_than_10ms = np.sum(intervals < 10)
    longer_than_10ms = np.sum(intervals > 10)

    if longer_than_10ms == 0:
        return 0

    Rb = shorter_than_10ms / longer_than_10ms
    return Rb


"""
    Standard deviation of durations of intervals between spikes
"""


def standard_deviation_of_duration(intervals):
    return np.std(intervals)


"""
    Signal power in the low and high frequency bands.
"""


def signal_power(data, f=20000, low_band=(0, 500), high_band=(500, 3000)):
    # Perform FFT
    N = len(data)
    T = 1.0 / f
    yf = fft(data)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

    # Power spectrum
    power_spectrum = 2.0 / N * np.abs(yf[:N // 2])

    # Low frequency band power
    low_band_power = np.sum(power_spectrum[(xf >= low_band[0]) & (xf < low_band[1])])

    # High frequency band power
    high_band_power = np.sum(power_spectrum[(xf >= high_band[0]) & (xf <= high_band[1])])

    return low_band_power, high_band_power


"""
    Average Nonlinear Energy'
    ANE = 1/(N-2) * sum(|xi^2 - xi+1 * xi-1|)
"""


def average_nonlinear_energy(data):
    N = len(data)
    sum = 0.0
    for i, value in enumerate(data):
        if i < N - 1:
            sum += abs(value ** 2 - data[i + 1] * data[i - 1])

    ANE = (1 / (N - 2)) * sum
    return ANE


"""
    Average Absolute Difference
    AAD = 1/(N-2) * sum(|xi - mean|)
"""


def average_absolute_difference(data):
    N = len(data)
    mean_value = np.mean(data)
    AAD = (1 / (N - 2)) * np.sum(np.abs(data[1:-1] - mean_value))
    return AAD


"""
    Root Mean Square
    RMS = sqrt(1/N * sum(xi^2))
"""


def rms(data):
    return np.sqrt(np.mean(np.square(data)))
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

# Calculating threshold based on neighbouring segments
def calculate_treshold(data, segment, segment_size, i):
    left_neighbour_segment = 10
    right_neighbour_segment = 10
    if i < left_neighbour_segment:
        left_neighbour_segment = i
    elif i + right_neighbour_segment > len(data) // segment_size:
        right_neighbour_segment = len(data) // segment_size - i - 1

    if left_neighbour_segment + right_neighbour_segment <= 1:
        return np.nan

    segment_data = data.iloc[(i - left_neighbour_segment) * segment_size : (i + 1 + right_neighbour_segment) * segment_size]["2: preprocessed"]
    if len(segment_data) > 1:
        threshold = 7 * np.std(segment_data.dropna())
    else:
        threshold = np.nan

    return threshold

def data_without_extreme_spikes(data, segment_size, ax_to_plot_threshold=None):
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
        if np.isnan(threshold):
            continue

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

        if ax_to_plot_threshold is not None:
            start_index = i * segment_size
            end_index = min((i + 1) * segment_size, len(data['Time']))
            ax_to_plot_threshold.plot([data['Time'].iloc[start_index], data['Time'].iloc[end_index - 1]],
                                      [threshold, threshold], color='r',
                                      linestyle='--', linewidth=0.5)

    if previous_was_accepted:
        ranges['end_time'].append(last_end_time)

    for i in range(len(ranges['start_time'])):
        print(f"Start: {ranges['start_time'][i]}, End: {ranges['end_time'][i]}")

    start, end = get_longest_range(ranges)
    return start, end

