from abc import ABC,abstractmethod

class insecets(ABC):
    def move(self):
        pass
    
class spider(insecets):
        def print(self):
            print("i have 8 legs")
            
class ant(insecets):
        def print(self):
            print("i have 2 antenas")
class centipeds(insecets):
        def print(self):
            print("i have 100 legs")
class millipeds(insecets):
        def print(self):
            print("i have 1000 legs")
            
R = spider
R.move()

k = ant
k.move()

R = centipeds
R.move()

k = millipeds
k.move()
