import numpy as np
import cv2
count = 1
def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('frame')
    

    while(True):
        ret, frame = cap.read()
        cv2.setMouseCallback('frame',captureFrame,frame)

        print('hi')

        

        

        if ret:
            cv2.imshow('frame',frame)
            global count
            if count == 2:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def captureFrame(event,x,y,flags,frame):
    global count 
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.imwrite('test.jpg',frame) # want to save frame here
        print(count)
        count=2
        print(count)

        


if __name__ == "__main__":
    main()
