file_read=open('mowaffa.txt'r'')
print("file in read mode")
print(file_read.read())

file_read.close()

file_write=open('mowaffa.txt','w')
file_write.write("file in write mode")
file_write.write("hi i am a codingal student i am 12 years old")

file_write.close()



file_append=open('mowaffa.txt','a')
file_append.write("\n file in append mode")
file_append.write("hi i am a codingal student i am 12 years old")

file_append.close()