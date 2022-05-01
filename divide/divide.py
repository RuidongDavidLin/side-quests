import cv2
vidcap = cv2.VideoCapture('5.MP4')
success,img = vidcap.read()
count = 554 
success = True
while success :
    success,image = vidcap.read()
    cv2.imwrite("frame%d.jpg" % count, image)
    if cv2.waitKey(10) == 27:
        break
    count += 1
