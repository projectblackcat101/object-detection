import os
import datetime

def rename():
    dt = str(datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
    dt1 = str(datetime.datetime.today())
    Current_Date = datetime.datetime.now()
    Current_Date =Current_Date.strftime("%d/%m/%Y %H:%M:%S")
    c=str(Current_Date)    
    newname='image_'+dt+'.jpg'
    os.rename('./save/test_soya.jpg','./save/'+newname)

