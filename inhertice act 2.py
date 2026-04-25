class Person:
    
        def __init__(self,fname,lname):
            self.fname = fname
            self.lname = lname
            
        def printnmae(self):
            print(self.firsame,self.lastname)
        
            
class Student(Person):
                  
          def __init__ (self,fname,lname,year):
                 
            super().__init__ (self,fname,lname)
            self.graduationyear= year      
              
              
a = Student("Mowaffak","Al jiroudi",2015)

a.printnmae()
print(a.graduationyear)