file = open('Codingal.txt','r')
print(file.read())
file.close


file = open('Codingal.txt','r')
print("\n in read parts \n")
print(file.read(8))
file.close()


file = open('Codingal.txt','a')
print("Hi i am a penguin andd i am 1yr old")
file.close()
