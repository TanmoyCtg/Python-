class Car:
  name = ""
  color = ""
  #when the object is made, it's automatically called init method
  #it's a constructor of python
  def __init__(self,name,color):
    self.name = name
    self.color = color
  
  def start(self):
    print ("Starting the engine")
  
myCar = Car("Corolla","white")
print (myCar.name)
print(myCar.color)
myCar.start()
