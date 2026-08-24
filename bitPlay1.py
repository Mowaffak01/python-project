input("set a bit - OR it turns ON. Press enter")
print("5 =",bin(5)[2:])
print("5 | 2 =", 5|2 ,"binary:", bin (5|2)[2:] )

input("Zero a bit - AND it turns OFF. Press enter")
print("7 =",bin(7)[2:])
print("7 & 5 =", 7 & 5 ,"binary:", bin (7 & 5)[2:] )

n = int(input("Enter a number (Try 4 or 6 )"))

guess = input("is it a power of 2 yes/no ?")
input("power of 2 - only one bit is ON. Press enter")
if n > 0 and (n &(n- 1))==0:
    print("", n ,"binary :",bin(n)[2:],"power of 2 your guess:",guess)
else:
     print("", n ,"binary :",bin(n)[2:],"not power of 2  your guess:",guess)

