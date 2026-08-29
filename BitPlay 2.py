input("XOR with zero keeps the number. Press enter")
print(" 5 ^ 0 = ",5 ^ 0)
print("9 ^ 0 = ",9 ^ 0)

input("XOR with itself makes 0. Press enter")
print(" 5 ^ 5 = ",5 ^ 5)
print("9 ^ 9 = ",9 ^ 9)

n = int(input("Enter a number (Try 6 or 11 )"))
guess = input("what is 3 ^ =" + str(n) + " ^ 3?")
input("XOR cancels - 3 appears twice so it disapers. Press enter")
print("3 ^", n ,"^ 3 = ",3^n^3," your guess:",guess)