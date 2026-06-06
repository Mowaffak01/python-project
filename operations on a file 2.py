with open('Codingal.txt','w')as file:
 file.write("hi there i am a penguin and i am 1 years old. ")
 file.close
 
 with open('Codingal.txt','r')as file:
     data = file.readlines()
     print("words in this file are")
     for line in data:
      word  = line.split()
      print(word)
      file.close