outputfile = open("List.txt",'w')
inputfile = open("mowaffa.txt",'r')

lines_seen_so_far = set()
print("elimanating Lines")
for line in inputfile:
    
    if line not in lines_seen_so_far:
        
        outputfile.write(line)
        
lines_seen_so_far.add(line)

outputfile.close()
inputfile.close()