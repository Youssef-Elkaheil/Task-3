from PyQt5.QtWidgets import QFileDialog, QLabel, QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore
from ImgModel import ImageModel
from Modes import Modes
import numpy as np
import logging
import UI
import sys
import cv2

class image(object):
    def __init__(self, MainWindow):
        super(image, self).setupUi(MainWindow)

        self.filepath = ["", ""]
        self.images = [[], []]
        self.image_no = [0, 0]
        self.data = []
        self.output_no = 0
