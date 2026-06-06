
file1= open('Codingal.txt','r')

file2= open('List.txt','r')


for line in file1.readlines():
    
     if not (linestartswith('Coding')):
         
         print (line)
         
         file2.write(line)
         
file2.close

file1.close