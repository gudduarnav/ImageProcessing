# Sketch Filter
# Import Module

try:
    import cv2
except ImportError as ex:
    print("Install cv2. Exception:", str(ex))
    exit(1)

try:
    import numpy as np
except ImportError as ex:
    print("Install numpy. Exception:", str(ex))
    exit(1)


def dodge(image, mask):
    return cv2.divide(image, 255-mask, scale=256)

def burn(image, mask):
    return 255-cv2.divide(255-image, 255-mask, scale=256)


# Convert the image RGB matrix to sketch matrix
def sketchme(im, imCanvas=None, rect=(21,21), sigmaX=0, sigmaY=0, masking=dodge):
    im1 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im2 = 255-im1
    im3 = cv2.GaussianBlur(im2, ksize=rect, sigmaX=sigmaX, sigmaY=sigmaY)
    im4 = masking(im1, im3)
    if imCanvas is not None:
        shape = im1.shape
        imCanvas1 = cv2.cvtColor(imCanvas, cv2.COLOR_BGR2GRAY)
        imCanvas2 = cv2.resize(imCanvas1, (shape[1], shape[0]), cv2.INTER_CUBIC)
        im4 = cv2.multiply(im4, imCanvas2, scale=1.0/256.0)
    return im4




