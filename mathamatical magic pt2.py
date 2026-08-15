def sieveoferatosthemes(number):
    prime = [True for i in range(number+ 1)]
    p = 2
    while ( p*p <= number ):
        if (prime[p] == True):
            for i in range (p*p,number + 1 ,p):
                prime[i] = False
                p += 1
                
                for p in range  (2,number +1):
                    if prime [p]:
                        print(p)
                    number= int(input("Enter a number : "))
                    print("following are prime number smallest")
                    print("than or equal to",number)
                    sieveoferatosthemes(number)
    
                