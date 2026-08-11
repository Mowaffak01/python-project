number = int(input("Enter your number :"))
orignal_number = number
reversed_number = 0

while number > 0:
    digt = number % 10 
    reversed_number = reversed_number * 10 + digt
    number //=10
     
if orignal_number == reversed_number:
    print (f"{orignal_number}is a plaidrome")
else:
     print (f"{orignal_number}is  not a plaidrome")
          