number = int(input("input your number :"))
digits = len(str(number))
reslutnumber = 0
temp = number
while temp > 0:
    digit = temp % 10
    reslutnumber += digit**digits
    temp //= 10
    
    
if number == reslutnumber:
    print(number,"is an armstrong number")
else:
    print(number," is not an armstrong number")