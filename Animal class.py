from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass
    
class human(animal):
        def print(self):
            print("i can walk")
            
class snake(animal):
        def print(self):
            print("i can crawal")
class dog(animal):
        def print(self):
            print("i can bark")
class lion(animal):
        def print(self):
            print("i can roar")
            
R = human
R.move()

k = snake
k.move()

R = dog
R.move()

k = lion
k.move()