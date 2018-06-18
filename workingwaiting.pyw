#!C:\Users\tlancon\Documents\FILES\Library\Tools\WorkingWaiting\venv\Scripts\pythonw.exe

import os
import sys
import time
from PyQt5 import QtCore, QtWidgets, uic

qtCreatorFile = os.path.abspath('workingwaiting.ui')

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.workingSeconds = 0
        self.workingTotal = 0
        self.workingTimer = QtCore.QTimer()
        self.workingTimer.timeout.connect(self.workingCounter)

        self.waitingSeconds = 0
        self.waitingTotal = 0
        self.waitingTimer = QtCore.QTimer()
        self.waitingTimer.timeout.connect(self.waitingCounter)

        self.workingButton.clicked.connect(self.work)
        self.waitingButton.clicked.connect(self.wait)
        self.resetButton.clicked.connect(self.reset)
        self.stopButton.clicked.connect(self.stop)

        self.resetButton.setEnabled(False)
        self.stopButton.setEnabled(False)

        self.intervalCounter = 0

        self.reset()

    def workingCounter(self):
        self.workingSeconds += 1
        self.workingTotal += 1
        self.currentWorkingValue.setText(str(self.workingSeconds))
        self.totalWorkingValue.setText(str(self.workingTotal))

    def waitingCounter(self):
        self.waitingSeconds += 1
        self.waitingTotal += 1
        self.currentWaitingValue.setText(str(self.waitingSeconds))
        self.totalWaitingValue.setText(str(self.waitingTotal))

    def work(self):
        self.waitingTimer.stop()
        self.workingSeconds = 0
        self.waitingSeconds = 0
        self.workingTimer.start(1000)
        self.workingButton.setEnabled(False)
        self.waitingButton.setEnabled(True)
        self.stopButton.setEnabled(True)
        self.updateStats('Working')

    def wait(self):
        self.workingTimer.stop()
        self.workingSeconds = 0
        self.waitingSeconds = 0
        self.waitingTimer.start(1000)
        self.waitingButton.setEnabled(False)
        self.workingButton.setEnabled(True)
        self.stopButton.setEnabled(True)
        self.updateStats('Waiting')

    def stop(self):
        self.workingTimer.stop()
        self.waitingTimer.stop()
        self.workingButton.setEnabled(True)
        self.waitingButton.setEnabled(True)
        self.resetButton.setEnabled(True)
        self.updateStats('Stopped')

    def updateStats(self, status):
        if self.intervalCounter is not 0:
            self.outputWindow.append('Total Working: {}'.format(self.workingTotal))
            self.outputWindow.append('Total Waiting: {}'.format(self.waitingTotal))
        self.intervalCounter += 1
        self.outputWindow.append('Interval {}: {} at {}'.format(self.intervalCounter, status, time.strftime('%x %X')))

    def reset(self):
        self.workingTimer.stop()
        self.workingSeconds = 0
        self.workingTotal = 0
        self.currentWorkingValue.setText(str(self.workingSeconds))
        self.totalWorkingValue.setText(str(self.workingTotal))
        self.workingButton.setEnabled(True)
        self.waitingTimer.stop()
        self.waitingSeconds = 0
        self.waitingTotal = 0
        self.currentWaitingValue.setText(str(self.waitingSeconds))
        self.totalWaitingValue.setText(str(self.waitingTotal))
        self.waitingButton.setEnabled(True)
        self.outputWindow.setText('')
        self.stopButton.setEnabled(False)
        self.intervalCounter = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())