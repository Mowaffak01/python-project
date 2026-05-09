class Tablet:
    
        def __init__(self):
            self.highsetprice = 750
            
        def sell(self):
            print("price.{}".formal(self.__highsetprice))
        def sethighsetprice(self,price):
            self.__highsetprice - price
            
c = Tablet()
c.sell()

c.__highsetprice = 900
c.sell()


c.sethighsetprice(900)
c.sell()
            