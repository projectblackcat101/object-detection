from tkinter import *
import tkinter as tk
import mysql.connector
from mysql.connector import Error
import cv2
window=Tk()
window.geometry("500x300")
window.title("testing")
soya=0
mitti=0
kadi=0
grade='A'
filename='s'
count = 1

def show_ans(ansDict):#added
    global soya
    global mitti
    global kadi
    ans1 = 'total count: '+str(ansDict['total'])
    ans2 = 'kadi count: '+str(ansDict['kadi_count'])
    ans3 = 'matti cont: '+str(ansDict['matti_count'])
    ans4 = 'soya count: '+str(ansDict['soya_count'])
    soya=ansDict['soya_count']
    mitti = ansDict['matti_count']
    kadi = ansDict['kadi_count']
    
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
    global_dict = ansDict
    show_ans(ansDict)
    import rename
    import move
    move.move()
    filename=rename.rename()
    print(filename)
    print(kadi)
    mysql(filename,soya,kadi,mitti,grade)
    



def capture():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('frame')
    

    while(True):
        ret, frame = cap.read()
        cv2.setMouseCallback('frame',captureFrame,frame)
        
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
        cv2.imwrite('test_soya.jpg',frame) # want to save frame here
        
        count=2
        

def mysql(filename,soya,kadi,mitti,grade):
      import mysql.connector
      mydb = mysql.connector.connect(
      host="db4free.net",
      user="projectblackcat",
      passwd="projectblackcat@123",
      database="pythonproject")
      mycursor = mydb.cursor()
      
      sql = "INSERT INTO obj (imagename, soya,kadi,mitti,grade) VALUES (%s,%s,%s, %s ,%s)"
      val = (filename, soya,kadi,mitti,grade)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      sql_select_Query = ("SELECT id FROM `obj` WHERE imagename= '%s' " %filename)
      mycursor.execute(sql_select_Query)
      records = mycursor.fetchall()
      print("\nPrinting Id")
      for row in records:
            print("Id = ", row[0], )
            id=row[0]
            print(id)
            up = 'Save this id for future refrence: '+str(id)
            l5 = Label(window,text = up)
            l5.pack()

      mydb.close()
      mycursor.close()
      print("MySQL connection is closed")



def id(filename):
    id=0
    try:
        connection = mysql.connector.connect( host="db4free.net",
                                              user="projectblackcat",
                                              passwd="projectblackcat@123",
                                              database="pythonproject")

        sql_select_Query = ("SELECT id FROM `obj` WHERE imagename= '%s' " %filename)
        print(sql_select_Query)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        print("Total number of rows in Table is: ", cursor.rowcount)

        print("\nPrinting Id")
        for row in records:
            print("Id = ", row[0], )
            id=row[0]
            print(id)
            l5 = Label(window,text = id)
            l5.pack()

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

    
def exitt():
    
    exit()



    


b1=Button(window,text="capture",width=15,bg='brown',fg='white',command=capture)
b1.place(x=100,y=150)

b2=Button(window,text="predict",width=15,bg='brown',fg='white',command=prediction)
b2.place(x=250,y=150)

b3=Button(window,text="exit",width=15,bg='brown',fg='white',command=exitt)
b3.place(x=175,y=250)

window.mainloop()
