# Convert an video to sketch

try:
    import cv2
except Exception as ex:
    print("Install cv2. Exception:", str(ex))
    exit(1)

from sketch import sketchme, dodge, burn


def main():
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Sketch", cv2.WINDOW_NORMAL)

    im_canvas = cv2.imread("canvas.jpg")

    cap = cv2.VideoCapture(0)
    print("Press any key to quit...")

    while True:
        result, im = cap.read()
        im = cv2.flip(im, 1)
        im_sketch = sketchme(im=im, imCanvas=im_canvas, masking=dodge)

        cv2.imshow("Original", im)
        cv2.imshow("Sketch", im_sketch)

        if not result:
            print("No Video")
            break

        if cv2.waitKey(50) & 0xFF == ord("q"):
            print("quitting")
            break

    cv2.destroyAllWindows()
    print("DONE")



if __name__ == "__main__":
    main()