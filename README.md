#HW1 ANCHERY DETECTION

#### Introduction 

There are three different ways to accomplish this project.
Please install opencv in advanced.

####Usage
1. First one is **Color-base** approach. The output video will be in _.output/color-based_ folder

'''shell
	python color-based.py -p <video_name>.mp4
'''
(color-based.jpg)
2. Second one is **Hough_base** approach. The output video will be in _.output/hough_based_ folder
'''shell
	python hough-based.py -p <video_name>.mp4
'''
(hough_based.jpg)
3. Last approch is developed by myself. The output video will be in _.output/own_solved_ folder
'''shell
	python own_solved.py -p <video_name>.mp4
'''
(own_solved.jpg)
####Conclusion
The results from my own approach can almost detect the countour of yellow, but the blue part of the anchery cannot work out. I suspect that one of the problem is maybe the hand holding on the anchery makes my algorithm more difficult to detect as a circle. 
