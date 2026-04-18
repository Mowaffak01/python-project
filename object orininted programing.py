class student:
     grade = 10
     name ="penguin"
     
     def introduction(self):
         print("hi I am a student")
         
     def details (self):
         print("my name is",self.name)
         print("i study in Grade",self.grade)
         
ob = student()
ob.introduction()
ob.details()