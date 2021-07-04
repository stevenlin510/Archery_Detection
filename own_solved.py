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

out = cv2.VideoWriter('./output/own_solved/'+ video_name,cv2.VideoWriter_fourcc(*"mp4v"),fps,(frame_width,frame_height))
center_y = None
t=0
while True:

	ret, frame = video.read()
	if ret is False:
		break

	if t ==1:
		break
	t+=1

	img = frame.copy()
	mor = frame.copy()
	# cv2.imwrite('original.jpg',frame)
	kernel = np.ones((5,5),np.uint8)

	closing = cv2.morphologyEx(mor, cv2.MORPH_CLOSE, kernel)

	closed = cv2.add(closing,img)

	hsv = cv2.cvtColor(closed,cv2.COLOR_BGR2HSV)

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

	

	for cnt in yellow_cnts:
	    approx_y = cv2.approxPolyDP(cnt, .03*cv2.arcLength(cnt, True), True)
	    ky=cv2.isContourConvex(approx_y)
	    area_y = cv2.contourArea(cnt)
	    if ky & (len(approx_y)>5) & (area_y > 50):
	    	(cx, cy), radius = cv2.minEnclosingCircle(cnt)
	    	center_y = (int(cx),int(cy))
	    	radius = int(radius)
	    	frame = cv2.circle(frame,center_y,radius,(0,0,255),2)


	for cnt in blue_cnts:
	    approx_b = cv2.approxPolyDP(cnt, .03*cv2.arcLength(cnt, True), True)
	    kb=cv2.isContourConvex(approx_b)
	    area_b = cv2.contourArea(cnt)	 
	    if kb & (len(approx_b)>5) & (area_b > 75):
	    	(cx, cy), radius = cv2.minEnclosingCircle(cnt)
	    	center_b = (int(cx),int(cy))
	    	radius = int(radius)
	    	if center_y is None:
	    		pass
	    	else:
		    	diff = (np.diff([center_b, center_y],axis=0) ** 2).sum()
		    	if diff < 200:	    	
		    		frame = cv2.circle(frame,center_b,radius,(0,0,255),2)




	# cv2.imwrite('closing.jpg',closing)
	cv2.imwrite('own_solved1.jpg',frame)
	
	# cv2.imshow('img',frame)

	cv2.waitKey()
	out.write(frame)

video.release()
out.release()

