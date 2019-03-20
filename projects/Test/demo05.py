"""
    Created by 朝南而行 2019/3/19 14:05
"""
import cv2
import zlib
import os

cap = cv2.VideoCapture('a.swf')
c=0
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    cv2.imwrite('image/'+str(c) + '.jpg', frame) #存储为图像
    c=c+1
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()