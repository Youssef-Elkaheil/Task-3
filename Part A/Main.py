from PyQt5.QtWidgets import QFileDialog, QLabel, QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore
from ImgModel import ImageModel
from Modes import Modes
import numpy as np
import logging
import UI
import sys
import cv2

# Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()

class ImageMixer(UI.Ui_MainWindow):

    def __init__(self,MainWindow):
        super(ImageMixer,self).setupUi(MainWindow) 
        
    def open(self, flag):
        
        logger.info("Browsing the files...")
        repo_path = "images"
        self.filepath[flag], _ = QtWidgets.QFileDialog.getOpenFileName(None, "Load Image", repo_path,
                                                                        "*.jpg;;" "*.jpeg;;" "*.png;;")
        self.path = self.filepath[flag]
        logger.info("Image"+str(flag+1)+" opened correctly")
        self.img = cv2.cvtColor(cv2.imread(self.path), cv2.COLOR_BGR2GRAY)
        self.images[flag] = ImageModel(self.path)
        self.showComponent[flag].setCurrentIndex(0)
        self.img_viewers[flag+2].clear()
        self.view_image(self.img, flag)
        self.check_size()
        logger.info("Image"+str(flag+1)+"  is ploted")


    def check_size(self):
        if self.images[0] != [] and self.images[1] != []:
            if self.images[0].imgShape != self.images[1].imgShape:
                self.enable(False)
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("The two images are of different size")
                logger.warning("The two images are of different size")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
            else:
                self.enable(True)

    def view_image(self, data, imgflag):
        self.img_viewers[imgflag].setImage((data).T)
        self.img_viewers[imgflag].view.setRange(xRange=[0, self.images[0].imgShape[0]], yRange=[0, self.images[0].imgShape[1]],
                                           padding=0)
        self.img_viewers[imgflag].view.setAspectLocked(False)
        logger.info("Data is ploted")

    def img_options(self, imgflag):
        if self.showComponent[imgflag].currentText() == "Magnitude":
            self.data = self.images[imgflag].magnitude2
            logger.info("Magnitude has been selected")
        elif self.showComponent[imgflag].currentText() == "Phase":
            self.data = self.images[imgflag].phase
            logger.info("Phase has been selected")
        elif self.showComponent[imgflag].currentText() == "Real":
            self.data = self.images[imgflag].real2
            logger.info("Real has been selected")
        elif self.showComponent[imgflag].currentText() == "Imaginary":
            self.data = self.images[imgflag].imaginary
            logger.info("Imaginary has been selected")
        else:
            logger.warning("No component has been selected")      
        self.view_image(self.data, imgflag+2)

    def mix_options(self, flag=0):
        for n in range(2):
            self.Percentage[n].setText("{}%".format(self.sliders[n].value()))
        self.Data = []
        if flag==1:
            self.comboxox_setitems()
        for i in range(2):
            if self.combobox_mixer[self.image_no[i]].currentText() == "Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Phase":
                self.Data = self.images[self.image_no[i]].mix(self.images[not(
                    self.image_no[i])], self.sliders[i].value(), self.sliders[not(i)].value(), Modes.magnitude_Phase)
                logger.info("Mix magnitude of image"+str(
                    self.image_no[i]+1)+" and phase of image" + str((self.image_no[not(i)])+1))

            elif self.combobox_mixer[self.image_no[i]].currentText() == "Real" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Imaginary":
                self.Data = self.images[self.image_no[i]].mix(self.images[not(
                    self.image_no[i])], self.sliders[self.image_no[i]].value(),
                        self.sliders[not(self.image_no[i])].value(), Modes.real_Imaginary)
                logger.info("Mix real of image"+str(
                    self.image_no[i]+1)+" and Imaginary of image" + str((self.image_no[not(i)])+1))

            elif self.combobox_mixer[self.image_no[i]].currentText() == "Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Uni Phase":
                self.Data = self.images[self.image_no[i]].mix(self.images[not(
                    self.image_no[i])], self.sliders[self.image_no[i]].value(),
                        self.sliders[not(self.image_no[i])].value(), Modes.magnitude_UniPhase)
                logger.info("Mix magnitude of image"+str(
                    self.image_no[i]+1)+" and uniphase of image" + str((self.image_no[not(i)])+1))

            elif self.combobox_mixer[self.image_no[i]].currentText() == "Uni Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Phase":
                self.Data = self.images[self.image_no[i]].mix(self.images[not(
                    self.image_no[i])], self.sliders[self.image_no[i]].value(),
                        self.sliders[1].value(), Modes.Unimagnitude_Phase)
                logger.info("Mix unimagnitude of image"+str(
                    self.image_no[i]+1)+" and phase of image" + str((self.image_no[not(i)])+1))

            elif self.combobox_mixer[self.image_no[i]].currentText() == "Uni Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Uni Phase":
                self.Data = self.images[self.image_no[i]].mix(self.images[not(
                    self.image_no[i])], self.sliders[self.image_no[i]].value(),
                        self.sliders[1].value(), Modes.uniMag_uniPhase)
                logger.info("Mix unimagnitude of image"+str(
                    self.image_no[i]+1)+" and uniphase of image" + str((self.image_no[not(i)])+1))

            else:
                logger.warning("Unavailable Mode")

        if len(self.Data) > 0:
            self.view_image(self.Data, self.output_no+4)
            logger.info("Mode is selected")
        else:
            logger.warning("No Mode is selected")

    def Mixer_img(self, boxflag):
        if self.Select_image[boxflag].currentText() == "Image 1":
            self.image_no[boxflag] = 0
        logger.info("Image1 is selected as input"+str(boxflag+1))
        if self.Select_image[boxflag].currentText() == "Image 2":
            self.image_no[boxflag] = 1
        logger.info("Image is selected as input"+str(boxflag+1))

    def output_img(self):
        if self.output.currentText() == "Output 1":
            self.output_no = 0
            logger.info("Display mixed image in output1")
        if self.output.currentText() == "Output 2":
            self.output_no = 1
            logger.info("Display mixed image in output2")

    def comboxox_setitems(self):
        self.combobox_mixer[1].clear()
        if self.combobox_mixer[0].currentText() == "Magnitude" or self.combobox_mixer[0].currentText() == "Uni Magnitude":
            self.combobox_mixer[1].addItem("Phase")
            self.combobox_mixer[1].addItem("Uni Phase")
        elif self.combobox_mixer[0].currentText() == "Phase" or self.combobox_mixer[0].currentText() == "Uni Phase":
            self.combobox_mixer[1].addItem("Magnitude")
            self.combobox_mixer[1].addItem("Uni Magnitude")
        elif self.combobox_mixer[0].currentText() == "Real":
            self.combobox_mixer[1].addItem("Imaginary")
        elif self.combobox_mixer[0].currentText() == "Imaginary":
            self.combobox_mixer[1].addItem("Real")
        logger.info("Combobox Itemtext changed")


def main():
    """
    the application startup functions
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ImageMixer(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


