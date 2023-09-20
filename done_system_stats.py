import sys
from PyQt5 import QtWidgets, QtCore
import psutil

class SystemMonitor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Monitor")
        self.cpu_label = QtWidgets.QLabel(self)
        self.ram_label = QtWidgets.QLabel(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.ram_label)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_usage_labels)
        self.timer.start(1000)  # Update every 1 second

    def get_cpu_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage

    def get_ram_usage(self):
        memory = psutil.virtual_memory()
        ram_usage = memory.percent
        return ram_usage

    def update_usage_labels(self):
        cpu_usage = self.get_cpu_usage()
        ram_usage = self.get_ram_usage()
        self.cpu_label.setText(f"CPU Usage: {cpu_usage}%")
        self.ram_label.setText(f"RAM Usage: {ram_usage}%")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    monitor = SystemMonitor()
    monitor.show()
    sys.exit(app.exec_())
