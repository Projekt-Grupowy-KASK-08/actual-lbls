""""# Define the paths to the CSV files
file_skorupa = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data_skorupa.csv'
file_zewnetrzne = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data_zewnetrzne.csv'
file_wewnetrzne = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data_wewnetrzne.csv'

# Read the CSV files
df_skorupa = pd.read_csv(file_skorupa)
df_zewnetrzne = pd.read_csv(file_zewnetrzne)
df_wewnetrzne = pd.read_csv(file_wewnetrzne)


# Function to compute features for each data frame


def compute_features(df):
    feature_results = {
        'average_frequency': [],
        'frequency_coefficient': [],
        'launch_rate': [],
        'pause_indicator': [],
        'pause_ratio': [],
        'modified_launch_rate': [],
        'std_duration': [],
        'low_band_power': [],
        'high_band_power': [],
        'average_nonlinear_energy': [],
        'average_absolute_difference': [],
        'rms': [],
        '80th_percentile': []
    }

    for index, row in df.iterrows():
        data = row.dropna().astype(float)
        spike_count, spike_indices = countSpikes(data)
        intervals = calculate_intervals(spike_indices)

        feature_results['average_frequency'].append(average_frequency_of_spikes(data))
        feature_results['frequency_coefficient'].append(frequency_coefficient(intervals))
        feature_results['launch_rate'].append(launch_rate(intervals))
        feature_results['pause_indicator'].append(pause_indicator(intervals))
        feature_results['pause_ratio'].append(pause_ratio(intervals))
        feature_results['modified_launch_rate'].append(modified_launch_rate(intervals))
        feature_results['std_duration'].append(standard_deviation_of_duration(intervals))

        low_band_power, high_band_power = signal_power(data)
        feature_results['low_band_power'].append(low_band_power)
        feature_results['high_band_power'].append(high_band_power)

        feature_results['average_nonlinear_energy'].append(average_nonlinear_energy(data))
        feature_results['average_absolute_difference'].append(average_absolute_difference(data))
        feature_results['rms'].append(rms(data))
        feature_results['80th_percentile'].append(np.percentile(data, 80))

    return feature_results


# Compute features for each data set
features_skorupa = compute_features(df_skorupa)
features_zewnetrzne = compute_features(df_zewnetrzne)
features_wewnetrzne = compute_features(df_wewnetrzne)

# Convert to DataFrame for easier plotting
df_features_skorupa = pd.DataFrame(features_skorupa).mean()
df_features_zewnetrzne = pd.DataFrame(features_zewnetrzne).mean()
df_features_wewnetrzne = pd.DataFrame(features_wewnetrzne).mean()

# Plotting the features
labels = df_features_skorupa.index
skorupa_values = df_features_skorupa.values
zewnetrzne_values = df_features_zewnetrzne.values
wewnetrzne_values = df_features_wewnetrzne.values

x = np.arange(len(labels))  # label locations
width = 0.25  # width of the bars

# Determine the number of rows and columns for the subplot grid
num_features = len(labels)
num_cols = 3
num_rows = (num_features + num_cols - 1) // num_cols

fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, 12))
axes = axes.flatten()  # Flatten the 2D array of axes to 1D for easy iteration

for i, label in enumerate(labels):
    axes[i].bar(['Skorupa', 'Zewnetrzne', 'Wewnetrzne'],
                [skorupa_values[i], zewnetrzne_values[i], wewnetrzne_values[i]],
                width)
    axes[i].set_title(label)
    axes[i].set_ylabel('Value')

# Remove any unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

fig.tight_layout()
plt.show()"""
import pandas as pd
from matplotlib import pyplot as plt

from signal_features import *

# Define the paths to the CSV files
file_skorupa = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data_skorupa.csv'
file_zewnetrzne = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data_zewnetrzne.csv'
file_wewnetrzne = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data_wewnetrzne.csv'

# Read the CSV files
df_skorupa = pd.read_csv(file_skorupa)
df_zewnetrzne = pd.read_csv(file_zewnetrzne)
df_wewnetrzne = pd.read_csv(file_wewnetrzne)


# Function to compute features for each data frame
def compute_features(df):
    feature_results = {
        'average_frequency': [],
        'average_frequency_of_spikes': [],
        'frequency_coefficient': [],
        'launch_rate': [],
        'pause_indicator': [],
        'pause_ratio': [],
        'modified_launch_rate': [],
        'std_duration': [],
        'low_band_power': [],
        'high_band_power': [],
        'average_nonlinear_energy': [],
        'average_absolute_difference': [],
        'rms': [],
        '80th_percentile': []
    }

    for index, row in df.iterrows():
        data = row.dropna().astype(float)
        spike_count, spike_indices = countSpikes(data)
        intervals = calculate_intervals(spike_indices)

        feature_results['average_frequency'].append(data.mean())
        feature_results['average_frequency_of_spikes'].append(average_frequency_of_spikes(data))
        feature_results['frequency_coefficient'].append(frequency_coefficient(intervals))
        feature_results['launch_rate'].append(launch_rate(intervals))
        feature_results['pause_indicator'].append(pause_indicator(intervals))
        feature_results['pause_ratio'].append(pause_ratio(intervals))
        feature_results['modified_launch_rate'].append(modified_launch_rate(intervals))
        feature_results['std_duration'].append(standard_deviation_of_duration(intervals))

        low_band_power, high_band_power = signal_power(data)
        feature_results['low_band_power'].append(low_band_power)
        feature_results['high_band_power'].append(high_band_power)

        feature_results['average_nonlinear_energy'].append(average_nonlinear_energy(data))
        feature_results['average_absolute_difference'].append(average_absolute_difference(data))
        feature_results['rms'].append(rms(data))
        feature_results['80th_percentile'].append(np.percentile(data, 80))

    return feature_results


# Compute features for each data set
features_skorupa = compute_features(df_skorupa)
features_zewnetrzne = compute_features(df_zewnetrzne)
features_wewnetrzne = compute_features(df_wewnetrzne)

# Convert to DataFrame for easier plotting
df_features_skorupa = pd.DataFrame(features_skorupa).mean()
df_features_zewnetrzne = pd.DataFrame(features_zewnetrzne).mean()
df_features_wewnetrzne = pd.DataFrame(features_wewnetrzne).mean()

# Plotting each feature in separate plots with different colors
labels = df_features_skorupa.index
skorupa_values = df_features_skorupa.values
zewnetrzne_values = df_features_zewnetrzne.values
wewnetrzne_values = df_features_wewnetrzne.values

# Set colors for the groups
colors = ['green', 'red', 'orange']
group_labels = ['Skorupa lub prążkowie', 'Czesci zewnętrzne gałki bladej \n (5-6 mm przed celem)',
                'Częsci wewnętrzne gałki bladej\n(2-3 mm przed celem\nlub do 1 mm za celem)']

# Descriptions for each feature (you can customize these descriptions)
feature_descriptions = {
    'average_frequency': 'Średnia częstotliwość sygnału',
    'average_frequency_of_spikes': 'Średnia częstotliwość występowania impulsów nerwowych',
    'frequency_coefficient': 'Współczynnik częstotliwości',
    'launch_rate': 'Częstotliwość uruchomienia',
    'pause_indicator': 'Wskaźnik pauzy',
    'pause_ratio': 'Stosunek pauz',
    'modified_launch_rate': 'Zmodyfikowana częstotliwość uruchomienia',
    'std_duration': 'Odchylenie standardowe czasu trwania',
    'low_band_power': 'Moc w niskim paśmie',
    'high_band_power': 'Moc w wysokim paśmie',
    'average_nonlinear_energy': 'Średnia nieliniowa energia',
    'average_absolute_difference': 'Średnia absolutna różnica',
    'rms': 'Średnia kwadratowa (RMS)',
    '80th_percentile': '80-ty percentyl wartości sygnału'
}

feature_descriptions_boxplot = {
    'average_frequency': 'Średnia częstotliwość sygnału',
    'average_frequency_of_spikes': 'Częstotliwość występowania impulsów nerwowych',
    'frequency_coefficient': 'Współczynnik częstotliwości',
    'launch_rate': 'Częstotliwość uruchomienia',
    'pause_indicator': 'Wskaźnik pauzy',
    'pause_ratio': 'Stosunek pauz',
    'modified_launch_rate': 'Zmodyfikowana częstotliwość uruchomienia',
    'std_duration': 'Odchylenie standardowe czasu trwania',
    'low_band_power': 'Moc w niskim paśmie',
    'high_band_power': 'Moc w wysokim paśmie',
    'average_nonlinear_energy': 'Średnia nieliniowa energia',
    'average_absolute_difference': 'Średnia absolutna różnica',
    'rms': 'Średnia kwadratowa (RMS)',
    '80th_percentile': '80-ty percentyl wartości sygnału'
}

# Y-axis labels for each feature (can be customized)
ylabels = {
    'average_frequency': 'Częstotliwość (Hz)',
    'average_frequency_of_spikes': 'Częstotliwość (Hz)',
    'frequency_coefficient': 'Współczynnik częstotliwości (Rf)',
    'launch_rate': 'Wskaźnik uruchomień (1/s)',
    'pause_indicator': 'Wskaźnik pauzy',
    'pause_ratio': 'Stosunek pauz (%)',
    'modified_launch_rate': 'Zmodyfikowana częstotliwość uruchomień',
    'std_duration': 'Odchylenie standardowe (ms)',
    'low_band_power': 'Moc (niskie pasmo)',
    'high_band_power': 'Moc (wysokie pasmo)',
    'average_nonlinear_energy': 'Nieliniowa energia',
    'average_absolute_difference': 'Średnia różnica absolutna',
    'rms': 'RMS (wartość skuteczna)',
    '80th_percentile': '80-ty percentyl'
}

for i, label in enumerate(labels):
    plt.figure(figsize=(8, 6))  # Create a new figure for each feature
    plt.bar(group_labels, [skorupa_values[i], zewnetrzne_values[i], wewnetrzne_values[i]],
            color=colors, width=0.4)
    plt.title(f'{feature_descriptions[label]}')
    plt.ylabel(f'{ylabels[label]}')
    plt.savefig(f'{feature_descriptions[label].lower()}.jpg')
    # plt.show()

labels = df_features_skorupa.index
skorupa_values = [features_skorupa[label] for label in labels]
zewnetrzne_values = [features_zewnetrzne[label] for label in labels]
wewnetrzne_values = [features_wewnetrzne[label] for label in labels]

for i, label in enumerate(labels):
    plt.figure(figsize=(10, 6))
    data_to_plot = [skorupa_values[i], zewnetrzne_values[i], wewnetrzne_values[i]]
    plt.boxplot(data_to_plot, labels=['Skorupa lub prążkowie', 'Części zewnętrzne gałki bladej \n (5-6 mm przed celem)',
                                      'Części wewnętrzne gałki bladej\n(2-3 mm przed celem\nlub do 1 mm za celem)'])
    plt.title(f'{feature_descriptions_boxplot[label]}')
    plt.ylabel(f'{ylabels[label]}')
    plt.savefig(f'{feature_descriptions_boxplot[label].lower()}_boxplot.jpg')
    plt.show()
