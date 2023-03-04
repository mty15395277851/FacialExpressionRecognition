import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFileDialog
from recognition_camera import load_model, generate_faces
from blazeface import blaze_detect
import numpy as np
from utils import index2emotion, cv2_img_add_text
from recognition_video import *

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.model = load_model()
        # create the label to display the video
        self.label = QLabel(self)
        self.label.setFixedSize(640, 480)

        file_name, file_type = QFileDialog.getOpenFileName(caption="选取图片", directory="./input/test/",
                                                           filter="All Files (*);;Text Files (*.txt)")

        predict_expression_1(file_name)

if __name__ == "__main__":
    app = QApplication([])
    player = VideoPlayer()
    app.exec_()
