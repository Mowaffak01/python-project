input("Bit difference - XOR shows which bits are differnt.  Press Enter")
print("5^3 =",5^3,"binary:",bin(5^3)[2:],"bits differnt:",bin(5^3).count('1'))
print("9^5 =",9^5,"binary:",bin(9^5)[2:],"bits differnt:",bin(9^5).count('1'))
n = int(input("Enter a number (try 4 or 6"))

guess = input("how many bits  differ between" + str(n) + "and 7?" )
input("XOR marks differnt bits -count 1s.  Press Enter")
diff = bin(n^7).count('1')
print("",n,"^7 = binary",bin(n^7)[2:],"differnt bits :",diff,"your guess",guess)