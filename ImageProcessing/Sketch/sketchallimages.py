from glob import glob
import os
from sketch import sketchme, burn, dodge

try:
    import cv2
except Exception as ex:
    print("Install cv2. Exception:", str(ex))
    exit(1)


in_dir = "./photos/"
out_dir = "./photos_out/"

if not os.path.isdir(in_dir):
    os.mkdir(in_dir)

if not os.path.isdir(out_dir):
    os.mkdir(out_dir)

files = glob(in_dir+"*.jpg")
total_counter = len(files)
counter=0

for image in files:
    counter = counter + 1
    s = "[{}/{}]".format(counter,total_counter)

    p= os.path.split(image)
    fname = p[-1]

    burn_fname =os.path.join(out_dir, "burn_"+fname)
    dodge_fname = os.path.join(out_dir, "dodge_"+fname)

    im1 = cv2.imread(image)
    print(s, fname, "read")
    im2 = sketchme(im1, masking=burn)
    im3 = sketchme(im1, masking=dodge)

    cv2.imwrite(burn_fname, im2)
    print(s, burn_fname, "written")

    cv2.imwrite(dodge_fname, im3)
    print(s, dodge_fname, "written")
