import datetime 
import os  
import shutil   
today = datetime.date.today()

today= str(today)

exp='2020-04-11'

def test():
    if today == exp:
        source = ( './s/test.txt')
        destination = ( './d/test.txt')
        dest = shutil.move(source, destination) 


