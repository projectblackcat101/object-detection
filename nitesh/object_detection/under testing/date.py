from datetime import datetime as dt
import os  
d1 = dt(2020,3,10) #yyyy,mm,dd
dcur= dt.now()
def test():
    if dcur >= d1:
        file1 = ( './s/test.txt') 
        if os.path.exists(file1):
            os.remove(file1)

#at one date copy content 
#at second date delete content 
