class Harshsrobot():
    
    machine = "robot"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
tom =Harshsrobot("tom",2 )
jerry =Harshsrobot("jerry",1)

print("i am tom a {}".format(tom.machine))
print("My brother jeery is also a {}".format(jerry.machine))

print("I  2 years old".format(tom.name,tom.age))
print("{} is   {} year old".format(jerry.name,jerry.age))