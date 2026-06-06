outputfile = open("Codingal.txt",'w')
inputfile = open("mowaffa.txt",'r')
lines_seen_so_far = set()
print("elimanating duplicate lines")
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        
lines_seen_so_far.add(line)
outputfile.close()
inputfile.close()