import cv2 
import numpy as np
import time

index = 0
cnt = 0
plateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

try:
    frame = cv2.imread('img.jpg')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plaques = plateCascade.detectMultiScale(gray, 1.3, 5)
    for i, (x, y, w, h) in enumerate(plaques):
        print()
        roi_color = frame[y:y + h, x:x + w]
        #cv2.putText(frame,str(x)+" "+ str(y)+" "+str(w)+" "+str(h), (480,220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
        r = 400.0 / roi_color.shape[1]
        dim = (400, int(roi_color.shape[0] * r))
        resized = cv2.resize(roi_color, dim, interpolation = cv2.INTER_AREA)
        w_resized=resized.shape[0]
        h_resized=resized.shape[1]
        cv2.imwrite(str(cnt) + '.jpg', resized)
        cnt += 1
        frame[100:100+w_resized,100:100+h_resized] = resized     
    cv2.destroyAllWindows()
except:
    pass
