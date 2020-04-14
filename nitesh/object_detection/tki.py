from tkinter import *
import tkinter as tk

window=Tk()
window.geometry("500x300")
window.title("testing")

def show_ans(ansDict):#added
    ans1 = 'total count: '+str(ansDict['total'])
    ans2 = 'kadi count: '+str(ansDict['kadi_count'])
    ans3 = 'matti cont: '+str(ansDict['matti_count'])
    ans4 = 'soya count: '+str(ansDict['soya_count'])
    l1 = Label(window,text = ans1)
    l2 = Label(window,text = ans2)
    l3 = Label(window,text = ans3)
    l4 = Label(window,text = ans4)
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()

def prediction():
    import Object_detection_image as odi
    ansDict = odi.get_ans()
    show_ans(ansDict)

def capture():
    print("Starting Camera")
    import cv2
    from time import sleep
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    
    sleep(2)
    while True:
     try:
        check, frame = webcam.read()
        #print(check) #prints true as long as the webcam is running
        #print(frame) #prints matrix values of each framecd
        #cv2.putText(frame, "Press s to save image", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        #cv2.putText(frame, "Press q to quit image", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='test_soya.jpg', img=frame)
            webcam.release()
            #print("Processing image...")
            #img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            #print("Converting RGB image to grayscale...")
            #gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            #print("Converted RGB image to grayscale...")
            #print("Resizing image to 28x28 scale...")
            #img_ = cv2.resize(gray,(300,300))
            #print("Resized...")
            #img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
            cv2.waitKey(0)
            cv2.destroyAllWindows()



            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

     except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break


def exitt():
    import rename
    import move
    move.move()
    rename.rename()
    exit()



    


b1=Button(window,text="capture",width=15,bg='brown',fg='white',command=capture)
b1.place(x=100,y=150)

b2=Button(window,text="predict",width=15,bg='brown',fg='white',command=prediction)
b2.place(x=250,y=150)

b3=Button(window,text="exit",width=15,bg='brown',fg='white',command=exitt)
b3.place(x=175,y=250)

window.mainloop()
