class bill:
    def __init__(self):
        self.unit=0
        self.amount=0
    def get_details(self):
        self.unit=""
        self.amount=0
    def calculate(self):
        self.unit=int(input("enter the unit"))
        self.amount=0
        if self.unit<=100:
          print("free")
        elif self.unit>100 and self.unit<=200:
          self.amount+=1.5*self.unit-100
        elif self.unit>200 and self.unit<=300:
          self.amount+=2.5*self.unit-100
        elif self.unit>300 and self.unit<=400:
         self.amount+=4*(self.unit)-100
        else:
          self.amount+=5*self.unit-100
        print("amount",self.amount)
S=bill()
S.get_details()
S.calculate()
