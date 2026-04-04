def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial (n-1)
num = int(input("enter a number"))
if num<0:
    print("srorry factural number does not exist for negative numbers")
    
elif num ==0:
    
    print("the factural number is 0 or 1")
    
else:
    print("the factural number of",num"is"recur_factorial(num))