import matplotlib.pyplot as plt
from skimage import io
from PIL import Image
import numpy as np
import cv2


class IndexDetection:
    def __init__(self, band4, band8):
        self.band4 = band4
        self.band8 = band8

    def normalization(self):
        self.band4 = cv2.normalize(self.band4, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        self.band8 = cv2.normalize(self.band8, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

        # Initial Index
        self.initialIndex()

    def initialIndex(self):
        # MSAVI
        # MSAVI= (2.0 * B08 + 1.0 - Math.sqrt(Math.pow((2.0 * B08 + 1.0), 2.0) - 8.0 * (B08 - B04))) / 2.0;
        self.MSAVI = (0.2 * self.band8 + 1 - np.sqrt(
            np.power((2 * self.band8 + 1), 2) - 8 * (self.band8 - self.band4))) / 2

        print("Min MSAVI: ", np.min(self.MSAVI))
        print("MAX MSAVI: ", np.max(self.MSAVI))

        # Plotting
        self.display()

    def display(self):
        cv2.imshow("MSAVI FILTER", self.band4)
        cv2.waitKey(0)

        # image = np.uint8(self.MSAVI)
        # cv2.imwrite('MSAVI.jpg', self.MSAVI)
        # image = cv2.imread('MSAVI.jpg')

        # plt.imshow(self.MSAVI)
        # plt.title('MSAVI Filter', fontsize=20)
        # plt.colorbar()
        # plt.axis('off')
        # plt.show()


if __name__ == '__main__':
    # Get Data
    # band4 = cv2.imread('Data/T40RCV_20220809T065631_B04.jp2')
    band44 = cv2.imread('T38RNU_20151226T074332_B04.jp2')
    band8 = cv2.imread('Data/T40RCV_20220809T065631_B08.jp2')
    my_object = IndexDetection(band44, band8)

    # Normalization
    my_object.normalization()
