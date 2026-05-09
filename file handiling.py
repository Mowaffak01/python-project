file = open('mowaffa.txt')
Counter = 0

Content = file.read

Colist = Content.split("\n")

for i in Colist:
    if i:
     Counter += 1
     
print("this is the number of lines in the file")
print(Counter)