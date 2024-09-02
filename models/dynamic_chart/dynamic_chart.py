import sys

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore

from models.dynamic_chart.csv_data_stream import csv_data_stream

CSV_FILEPATH = "/Users/pawelmanczak/Downloads/pacjenci/Wolf Krzysztof/546258766/depth1,5_kanalCentral.csv"
SAMPLING_RATE = 20_000  # Hz
NUM_OF_SECONDS_TO_DISPLAY = 4  # Duration of the visible window in seconds


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, csv_filepath):
        super().__init__()

        # values vs time dynamic plot
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.setBackground("w")
        styles = {"color": "red", "font-size": "18px"}
        self.plot_graph.setLabel("left", "mV", **styles)
        self.plot_graph.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph.addLegend()
        self.plot_graph.showGrid(x=True, y=True)
        # self.plot_graph.setYRange(20, 40)

        self.sampling_rate = SAMPLING_RATE
        self.time = np.arange(0,
                              SAMPLING_RATE * NUM_OF_SECONDS_TO_DISPLAY) / self.sampling_rate  # Time array in seconds
        self.values = [0] * len(self.time)  # Initialize values array with zeros

        pen = pg.mkPen(color='r', width=0.5)  # Line color and width
        self.line = self.plot_graph.plot(
            self.time,
            self.values,
            pen=pen,
        )

        chunk_size = 4000  # Number of samples to plot every update (200ms)
        self.data_stream = csv_data_stream(csv_filepath, self.sampling_rate, chunk_size)

        # Add a timer to simulate new values measurements
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)  # Update every 200 milliseconds (5 times per second)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Get new values from the CSV data stream
        new_values = next(self.data_stream)

        # Calculate new times corresponding to the new samples
        new_times = np.arange(len(new_values)) / self.sampling_rate + self.time[-1]

        # Append new times and values, removing the oldest ones
        self.time = np.concatenate((self.time[len(new_values):], new_times))
        self.values = self.values[len(new_values):] + list(new_values)

        # Update the plot with new data
        self.line.setData(self.time, self.values)

        # Update X-axis labels
        self.plot_graph.setLabel('bottom', 'Time (s)', **{"color": "red", "font-size": "18px"})


if __name__ == "__main__":
    filepath = CSV_FILEPATH
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow(filepath)
    main.show()
    sys.exit(app.exec_())
