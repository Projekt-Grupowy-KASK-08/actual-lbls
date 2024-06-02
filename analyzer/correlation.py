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
plt.show()
