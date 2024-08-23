import cv2 as cv
import numpy as np
import os
from utilities import * 

# processing images
path = "./Data"
img_list = getJPG(path) # get the name of all the images in certain dirctory with .jpg extension

# get the threshhold of the images
read_images = [cv.imread("Data/"+imgl) for imgl in img_list] # read the images from the image list
img_res = map(imgProcessing, read_images)
thresh_imgs = list(img_res)
radius,center = detectHole(thresh_imgs[2])
print(radius)
b, w = defects_detection(thresh_imgs[2], thresh_imgs[0], center)
print(b, w)
def main(ideal ,lstImg):
    ideal_radius, _ = detectHole(ideal)
    count = 2
    for img in lstImg:
        radius,center = detectHole(img)
        broken, worn = defects_detection(img, ideal, center)
        print("#"*30)
        print(f"The Data for the sample{count}")
        count += 1
        print(f"number of broken gear are:   {broken}")
        print(f"number of worn gear are:   {worn}")
        if abs(radius - ideal_radius) <= 3:
            print("the inner diameter is equevilant the the ideal sample")
        elif radius > ideal_radius:
            print("the inner diameter is greater the the ideal sample")
        elif radius < ideal_radius:
            print("the inner diameter is smaller the the ideal sample")
        
        print()
        print("#"*30)
        

main(thresh_imgs[0], thresh_imgs[1:])



cv.waitKey(0)
cv.destroyAllWindows()