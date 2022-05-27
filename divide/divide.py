import cv2
vidcap = cv2.VideoCapture('data.MP4')
success,img = vidcap.read()
count = 0 
success = True
while success :
    success,image = vidcap.read()
    cv2.imwrite("frame%05d.jpg" % count, image)
    if cv2.waitKey(10) == 27:
        break
    count += 1
