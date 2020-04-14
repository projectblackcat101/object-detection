# importing os module  
import os  
  
# importing shutil module  
import shutil  
  
# path  
#path = ('E:/testing bomb')
  
# List files and directories  
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'  
#print("Before moving file:")  
#print(os.listdir(path))  
  
  
def move(): 
    source = ( 'test_soya.jpg')
      
    # Destination path  
    destination = ( './save/test_soya.jpg')
      
    # Move the content of  
    # source to destination  
    dest = shutil.move(source, destination)  
  
# List files and directories  
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"  
#print("After moving file:")  
#print(os.listdir(path))  
  
# Print path of newly  
# created file  
#print("Destination path:", dest)

