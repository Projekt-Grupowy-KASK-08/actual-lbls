import sys

import numpy as np
import pandas as pd
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore

from models.dynamic_chart.csv_data_stream import csv_data_stream
from models.dynamic_chart.predict_from_saved_model import predict_from_saved_model

CSV_FILEPATH = "/Users/pawelmanczak/Downloads/pacjenci/Wolf Krzysztof/546258766/depth1,5_kanalCentral.csv"
SAMPLING_RATE = 20_000  # Hz
NUM_OF_SECONDS_TO_DISPLAY = 4  # Duration of the visible window in seconds

class PredictionWorker(QtCore.QThread):
    prediction_ready = QtCore.pyqtSignal(str)

    def __init__(self, new_values, index):
        super().__init__()
        self.new_values = new_values
        self.index = index

    def run(self):
        if self.new_values is not None:
            df_input_data = pd.DataFrame(self.new_values, columns=['Data'])
            predicted: str = str(predict_from_saved_model(df_input_data['Data'], depth=-1))
            self.prediction_ready.emit(predicted)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, csv_filepath):
        super().__init__()

        self.new_values = []
        self.prediction_thread = None
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.setBackground("w")
        styles = {"color": "red", "font-size": "18px"}
        self.plot_graph.setLabel("left", "mV", **styles)
        self.plot_graph.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph.showGrid(x=True, y=True)

        self.sampling_rate = SAMPLING_RATE
        self.window_duration = NUM_OF_SECONDS_TO_DISPLAY
        self.time = np.arange(0, self.window_duration * self.sampling_rate) / self.sampling_rate
        self.values = [0] * len(self.time)

        pen = pg.mkPen(color='r', width=0.1)  # Line color and width
        self.line = self.plot_graph.plot(self.time, self.values, pen=pen)

        chunk_size = 4000  # Number of samples to plot every update (200ms)
        self.data_stream = csv_data_stream(csv_filepath, self.sampling_rate, chunk_size)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)  # Update every 200 milliseconds (5 times per second)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.regions = []
        self.region_colors = []  # To store the colors of each region

        QtWidgets.qApp.aboutToQuit.connect(self.cleanup_threads)

    def update_plot(self):
        self.new_values = next(self.data_stream)

        new_times = np.arange(len(self.new_values)) / self.sampling_rate + self.time[-1]
        self.time = np.concatenate((self.time[len(self.new_values):], new_times))
        self.values = self.values[len(self.new_values):] + list(self.new_values)

        self.line.setData(self.time, self.values)
        self.plot_graph.setXRange(self.time[0], self.time[-1], padding=0)

        self.update_time_markers()

    def update_time_markers(self):
        current_time_range = (self.time[0], self.time[-1])
        num_seconds = int(current_time_range[1]) + 1  # Number of seconds to cover

        for region in self.regions:
            if region.getRegion()[1] < current_time_range[0]:
                self.plot_graph.removeItem(region)
        self.regions = [region for region in self.regions if region.getRegion()[1] >= current_time_range[0]]

        for i in range(len(self.regions), num_seconds):
            start_time = i
            end_time = i + 1
            if i < len(self.region_colors):
                color = self.region_colors[i]  # Use the stored color for this region
            else:
                if self.new_values is not None:
                    self.start_prediction_thread(i, self.new_values)

    def start_prediction_thread(self, index, new_values):
        if self.prediction_thread and self.prediction_thread.isRunning():
            self.prediction_thread.wait()  # Ensure previous thread is finished

        self.prediction_thread = PredictionWorker(new_values, index)
        self.prediction_thread.prediction_ready.connect(self.handle_prediction_result)
        self.prediction_thread.start()

    def handle_prediction_result(self, predicted):
        print("Predicted value as string:", predicted)
        if predicted == "['Skorupa lub prazkowie']":  # Compare with string "1"
            color = [20, 40, 30]
            self.region_colors.append(color)
            region = pg.LinearRegionItem(
                values=(len(self.region_colors) - 1, len(self.region_colors)),
                orientation='vertical',
                brush=pg.mkBrush(*color, alpha=10),  # Set the brush with the stored color and lower opacity
                pen=None  # No border for the regions
            )
            region.setZValue(-10)  # Ensure region is below the plot line
            self.plot_graph.addItem(region)
            self.regions.append(region)
        elif predicted == "['Czesci zewnetrzne galki bladej (5-6 mm przed celem)']":
            self.region_colors.append([60, 10, 80])
            region = pg.LinearRegionItem(
                values=(len(self.region_colors) - 1, len(self.region_colors)),
                orientation='vertical',
                brush=pg.mkBrush(255, 0, 0, alpha=10),  # Set the brush with the stored color and lower opacity
                pen=None  # No border for the regions
            )
            region.setZValue(-10)
            self.plot_graph.addItem(region)
            self.regions.append(region)

        else:
            self.region_colors.append([40, 10, 180])
            region = pg.LinearRegionItem(
                values=(len(self.region_colors) - 1, len(self.region_colors)),
                orientation='vertical',
                brush=pg.mkBrush(255, 0, 0, alpha=10),  # Set the brush with the stored color and lower opacity
                pen=None  # No border for the regions
            )
            region.setZValue(-10)
            self.plot_graph.addItem(region)
            self.regions.append(region)

    def cleanup_threads(self):
        if self.prediction_thread and self.prediction_thread.isRunning():
            self.prediction_thread.quit()
            self.prediction_thread.wait()


if __name__ == "__main__":
    filepath = CSV_FILEPATH
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow(filepath)
    main.show()
    sys.exit(app.exec_())
