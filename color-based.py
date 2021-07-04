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

out = cv2.VideoWriter('./output/color-based/1'+ video_name,cv2.VideoWriter_fourcc(*"mp4v"),fps,(frame_width,frame_height))
t=0
while True:

	ret, frame = video.read()
	if ret is False:
		break

	if t ==1:
		break
	t+=1
	img = frame.copy()

	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	blue_lr = np.array([90, 92, 2])
	blue_ur = np.array([130, 255, 150])
	blue_mask = cv2.inRange(hsv, blue_lr, blue_ur)

	# red_lr = np.array([164, 155, 84])
	# red_ur = np.array([179, 255, 255])
	# red_mask = cv2.inRange(hsv, red_lr, red_ur)

	yellow_lr = np.array([20, 136, 210])
	yellow_ur = np.array([40, 255, 255])
	yellow_mask = cv2.inRange(hsv, yellow_lr, yellow_ur)

	blue_cnts, _ = cv2.findContours(blue_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# red_cnts, _ = cv2.findContours(red_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	yellow_cnts, _ = cv2.findContours(yellow_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


	for cnt in blue_cnts:
	    area_b = cv2.contourArea(cnt)
	    if (area_b > 100):
		    (cx, cy), radius = cv2.minEnclosingCircle(cnt)
		    center = (int(cx),int(cy))
		    radius = int(radius)
		    frame = cv2.circle(frame,center,radius,(0,0,255),2)

	for cnt in yellow_cnts:
	    area_y = cv2.contourArea(cnt)
	    if (area_y > 50) :
	        (cx, cy), radius = cv2.minEnclosingCircle(cnt)
	        center = (int(cx),int(cy))
	        radius = int(radius)
	        frame = cv2.circle(frame,center,radius,(0,0,255),2)

	cv2.imwrite('color-based1.jpg',frame)
	# cv2.imwrite('closed.jpg',closed)

	out.write(frame)

video.release()
out.release()
