import sys
import os
# import multi_processing_starter

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from PyQt5 import QtWidgets

sys.path.append(os.path.dirname(__file__) + '/ui')
from ui_realtime import *
import multi_processing_starter


def printt():
    print("hello")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    detections = multi_processing_starter.Detections()
    menu_win = Realtime_Window()
    menu_win.show()

    sys.exit(app.exec_())
