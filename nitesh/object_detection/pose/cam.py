import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
count = 1
def main():
    #cap = cv2.VideoCapture(0)
    #cv2.namedWindow('frame')
    #count = 1

    while(True):
        ret, frame = cap.read()
        cv2.setMouseCallback('frame',captureFrame,frame)

        if ret:
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def captureFrame(event,x,y,flags,frame):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.imwrite('test.png',frame)
        cap.release()
        cv2.destroyAllWindows()
        exit()
         


#if __name__ == "__main__":
main()
