from Modes import Modes
import numpy as np
import cv2
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class ImageModel():

    """
    A class that represents the ImageModel
    """
    def __init__(self, imgPath: str):
        """
        :param imgPath: absolute path of the image
        """
        self.imagepath = imgPath
        self.img = cv2.cvtColor(cv2.imread(self.imagepath), cv2.COLOR_BGR2GRAY)
        self.imgShape = self.img.shape
        self.f = np.fft.fft2(self.img)
        self.fshift = np.fft.fftshift(self.f)
        self.magnitude = np.abs(self.fshift)
        self.magnitude2 = 20 * np.log(np.abs(self.fshift))
        self.phase = np.angle(self.fshift)
        self.real = np.real(self.fshift)
        self.real2 = 20 * np.log(np.real(self.fshift))
        self.imaginary = np.imag(self.fshift)
        self.uniPhase = np.zeros(self.imgShape)
        self.uniMagnitude = np.ones(self.imgShape)

    # def mix_options(self, flag=0):
    #     for n in range(2):
    #         self.Percentage[n].setText("{}%".format(self.sliders[n].value()))
    #     self.Data = []
    #     if flag == 1:
    #         self.comboxox_setitems()
    #     for i in range(2):
    #         if self.combobox_mixer[self.image_no[i]].currentText() == "Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Phase":
    #             self.Data = self.images[self.image_no[i]].mix(self.images[not(
    #                 self.image_no[i])], self.sliders[i].value(), self.sliders[not(i)].value(), Modes.magnitude_Phase)
    #             logger.info("Mix magnitude of image"+str(
    #                 self.image_no[i]+1)+" and phase of image" + str((self.image_no[not(i)])+1))

    #         elif self.combobox_mixer[self.image_no[i]].currentText() == "Real" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Imaginary":
    #             self.Data = self.images[self.image_no[i]].mix(self.images[not(
    #                 self.image_no[i])], self.sliders[self.image_no[i]].value(),
    #                 self.sliders[not(self.image_no[i])].value(), Modes.real_Imaginary)
    #             logger.info("Mix real of image"+str(
    #                 self.image_no[i]+1)+" and Imaginary of image" + str((self.image_no[not(i)])+1))

    #         elif self.combobox_mixer[self.image_no[i]].currentText() == "Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Uni Phase":
    #             self.Data = self.images[self.image_no[i]].mix(self.images[not(
    #                 self.image_no[i])], self.sliders[self.image_no[i]].value(),
    #                 self.sliders[not(self.image_no[i])].value(), Modes.magnitude_UniPhase)
    #             logger.info("Mix magnitude of image"+str(
    #                 self.image_no[i]+1)+" and uniphase of image" + str((self.image_no[not(i)])+1))

    #         elif self.combobox_mixer[self.image_no[i]].currentText() == "Uni Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Phase":
    #             self.Data = self.images[self.image_no[i]].mix(self.images[not(
    #                 self.image_no[i])], self.sliders[self.image_no[i]].value(),
    #                 self.sliders[1].value(), Modes.Unimagnitude_Phase)
    #             logger.info("Mix unimagnitude of image"+str(
    #                 self.image_no[i]+1)+" and phase of image" + str((self.image_no[not(i)])+1))

    #         elif self.combobox_mixer[self.image_no[i]].currentText() == "Uni Magnitude" and self.combobox_mixer[not(self.image_no[i])].currentText() == "Uni Phase":
    #             self.Data = self.images[self.image_no[i]].mix(self.images[not(
    #                 self.image_no[i])], self.sliders[self.image_no[i]].value(),
    #                 self.sliders[1].value(), Modes.uniMag_uniPhase)
    #             logger.info("Mix unimagnitude of image"+str(
    #                 self.image_no[i]+1)+" and uniphase of image" + str((self.image_no[not(i)])+1))

    #         else:
    #             logger.warning("Unavailable Mode")

    #     if len(self.Data) > 0:
    #         self.view_image(self.Data, self.output_no+4)
    #         logger.info("Mode is selected")
    #     else:
    #         logger.warning("No Mode is selected")

    
    def mix(self, imageToBeMixed: 'ImageModel', component1_ratio: float, component2_ratio: float, mode: 'Modes') -> np.ndarray:

        ratio1=component1_ratio/100
        ratio2=component2_ratio/100

        def output_transform (comp1,comp2):
            if mode == Modes.real_Imaginary:
            	Output_fourrier = comp1+(comp2*1j)
            else:
                Output_fourrier = comp1*np.exp(comp2*1j)
            Output = np.abs(np.fft.ifft2(np.fft.ifftshift(Output_fourrier)))
            logger.info("Transfromed components into time ")
            return Output

        if mode==Modes.magnitude_Phase:
            magnitude=self.magnitude*ratio1+(imageToBeMixed.magnitude*(1-ratio1))
            phase=imageToBeMixed.phase*ratio2+(self.phase*(1-ratio2))
            data=output_transform(magnitude,phase)
            logger.info("Mixing Magnitude and Phase")

        if mode==Modes.real_Imaginary:
            real=self.real*ratio1+(imageToBeMixed.real*(1-ratio1))
            imaginary=imageToBeMixed.imaginary*ratio2+(self.imaginary*(1-ratio2))
            data=output_transform(real,imaginary)
            logger.info("Mixing Real and Imaginary")

        if mode==Modes.magnitude_UniPhase:
            magnitude=self.magnitude*ratio1+(imageToBeMixed.magnitude*(1-ratio1))
            uni_phase=self.uniPhase 
            data=output_transform(magnitude,uni_phase)
            logger.info("Mixing Magnitude and UniPhase")

        if mode==Modes.Unimagnitude_Phase:
            uni_magnitude=self.uniMagnitude 
            phase=imageToBeMixed.phase*ratio2+(self.phase*(1-ratio2))
            data=output_transform(uni_magnitude,phase)
            logger.info("Mixing Unimagnitude and Phase")

        if mode==Modes.uniMag_uniPhase:
            uni_magnitude = self.uniMagnitude
            uni_phase = self.uniPhase
            data=output_transform(uni_magnitude,uni_phase)
            logger.info("Mixing UniMag and UniPhase")

        if(len(data) >0):
        	logger.info("Finished mixing")
        else: 
        	logger.info("no mixing")

        return data
