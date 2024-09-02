import pandas as pd

from models.random_forest.signal_features import *


def calculate_statistics_from_array(input_data, depth):
    """
    Calculate statistics from an array of data.
    Copy of the function from models/random_forest/signal_features.py

    :param input_data: array of data
    :param depth: depth of the data
    :return: DataFrame with statistics

    """
    statistics_list = []

    spike_count, spike_indices = countSpikes(input_data)
    avg_freq_spikes = average_frequency_of_spikes(input_data)
    intervals = calculate_intervals(spike_indices)
    freq_coeff = frequency_coefficient(intervals)
    launch_rt = launch_rate(intervals)
    pause_ind = pause_indicator(intervals)
    pause_rat = pause_ratio(intervals)
    mod_launch_rt = modified_launch_rate(intervals)
    std_duration = standard_deviation_of_duration(intervals)
    low_band_power, high_band_power = signal_power(input_data)
    avg_nl_energy = average_nonlinear_energy(input_data)
    avg_abs_diff = average_absolute_difference(input_data)
    root_mean_square = rms(input_data)
    mean_spike_hight = get_mean_spike_hight(input_data, spike_indices)

    statistics = [
        depth, spike_count, avg_freq_spikes, freq_coeff, launch_rt, pause_ind, pause_rat,
        mod_launch_rt, std_duration, low_band_power, high_band_power, avg_nl_energy,
        avg_abs_diff, root_mean_square, mean_spike_hight
    ]
    statistics_list.append(statistics)

    columns = [
        'depth', 'spike_count', 'avg_freq_spikes', 'freq_coeff', 'launch_rate', 'pause_indicator',
        'pause_ratio', 'mod_launch_rate', 'std_duration', 'low_band_power', 'high_band_power',
        'avg_nl_energy', 'avg_abs_diff', 'rms', 'mean_spike_hight'
    ]
    statistics_df = pd.DataFrame(statistics_list, columns=columns)

    return statistics_df
