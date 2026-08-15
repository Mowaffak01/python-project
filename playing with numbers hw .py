
numberBiggest = int(input("Enter the Largest number : "))

numberSmallest = int(input("Enter the Smallest number : "))
  
  
while(numberSmallest):
  numberStoreage = numberSmallest
  numberSmallest = numberBiggest % numberSmallest
  numberBiggest = numberStoreage
 
print("HCF is : ",numberBiggest)
