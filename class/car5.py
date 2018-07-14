class Car:
  
  def __init__(self,n,c):
    self.name = n
    self.color = c
  
  def start(self):
    print("name: ",self.name)
    print("color: ",self.color)
    print ("Starting the engine")
#make first car object  
myCar = Car("Corolla","white")
myCar.start()

#make 2nd car object
myCar1 = Car("Premio","Black")
myCar1.start()

#make 3rd car object
myCar2 = Car("Allion","Blue")
myCar2.start()

