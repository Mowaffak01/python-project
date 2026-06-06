new_file =('new_file.txt','x')
new_file.close()

import os
print("checking if file exists or not........")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")
        
    
new_file =('new file.txt','w')
new_file.write("hi i am a pengin and i am i yeas old")
new_file.close()
os.remove('codingal.txt')