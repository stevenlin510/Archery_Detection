import cv2
import numpy as np
import os,sys
import argparse
import matplotlib.pyplot as plt

sys.path.append('../')
parser = argparse.ArgumentParser()
parser.add_argument('--video_path','-p', type=str, required=True, help='video_path')

args = parser.parse_args()
video_path = args.video_path
video_name = video_path[5:]

video = cv2.VideoCapture(video_path)

frame_width = int(video.get(3))
frame_height = int(video.get(4))
fps = video.get(cv2.CAP_PROP_FPS)
t=0
out = cv2.VideoWriter('./output/hough_based/'+ video_name,cv2.VideoWriter_fourcc(*"mp4v"),fps,(frame_width,frame_height))
while True:

	ret, frame = video.read()
	if ret is False:
		break

	if t ==1:
		break
	t+=1
	img = frame.copy()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,70,param1=40,param2=30,minRadius=0,maxRadius=100)

	circles = np.uint16(np.around(circles))

	for i in circles[0,:]:
	    frame = cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)

	cv2.imwrite('hough_based1.jpg',frame)
	# cv2.waitKey()
	out.write(frame)

video.release()
out.release()
