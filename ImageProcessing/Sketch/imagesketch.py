# Convert an image to sketch

try:
    import cv2
except Exception as ex:
    print("Install cv2. Exception:", str(ex))
    exit(1)

from sketch import sketchme, dodge, burn


def main():
    im_orig = cv2.imread("tomjerry.jpg")
    im_canvas = cv2.imread("canvas.jpg")
    im_bw = sketchme(im=im_orig, imCanvas=im_canvas, masking=dodge)

    cv2.imshow("Original", im_orig)
    cv2.imshow("Sketch", im_bw)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()