import numpy as np 
import cv2

img = cv2.imread('pro.png', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150, 150), (255, 255, 255), 15) #opencv is BGR

cv2.rectangle(img, (15,25), (200,150), (255, 0, 0), 5)
cv2.circle(img, (100,63), 55, (0,255,0), -1)

pts = np.array([[10,5],[20,30],[70,30],[50, 10]],np.int32)


#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,0,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'OPENCV TUTS!', (0, 400), font, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()