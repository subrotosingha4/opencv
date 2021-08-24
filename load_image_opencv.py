#opencv tutorial link: https://docs.opencv.org/3.4.0/d6/d00/tutorial_py_root.html
# USAGE
# python load_image_opencv.py
# how to run the script
#python load_image_opencv.py --image birthday.png

#using command line is an efficient way to run a program and check the output on runtime

# import the necessary packages
import argparse #import argparse
import cv2 #import opencv to read image/load image

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser() #instantiate argparse as an object
ap.add_argument("-i", "--image", required=True,
	help="path to input image") #required true indicates you must need image and path to the image
args = vars(ap.parse_args()) #to pass an image from your pc you define the variable

# load the image from disk via "cv2.imread" and then grab the spatial
# dimensions, including width, height, and number of channels
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# display the image width, height, and number of channels to our
# terminal
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# show the image and wait for a keypress
cv2.imshow("Image", image) #Image indicates the title of the output image
cv2.waitKey(0) #waitkey to wait for a key to press

# save the image back to disk (OpenCV handles converting image
# filetypes automatically)
cv2.imwrite("newimage.jpg", image) #save the image as newimage.jpg