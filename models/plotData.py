import pandas as pd
import matplotlib.pyplot as plt

# Ścieżka do pliku CSV
filename = r'C:\Users\kasia\OneDrive\Pulpit\pacjenci\Sloma Pawel\466417777\depth-4,6_kanalCentral.csv'

start_time = 0.00545
end_time = 7.966150000000001
ranges = {
    'start_time': [0.00545, 2.24545],
    'end_time': [0.5187, 7.966150000000001]
}
print(ranges)
def plotData(filename, ranges):
    data = pd.read_csv(filename)
    data.columns = ['Time', 'raw', 'preprocessed']

    plt.figure(figsize=(15, 5))
    plt.plot(data['Time'], data['preprocessed'], label='Preprocessed', color='b', linewidth=0.5)
    plt.title('Raw vs. Time')
    plt.xlabel('Time (s)')
    for start, end in zip(ranges['start_time'], ranges['end_time']):
        plt.axvspan(start, end, color='gray', alpha=0.5)
    plt.ylabel('Preprocessed')
    plt.legend()
    plt.grid(True)
    plt.show()


plotData(filename, ranges)