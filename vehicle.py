class Vehicle:
    ''' def __init__() is Vehicle class constructor'''
    
    def __init__(self, name, manufacturer, color):
        print ("Creating a vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print ("Driving",self.manufacturer, self.name)

    def turn(self,direction):
        print ("Turning",self.name,"to",direction)

    def brake(self):
        print(self.name,"is stopping!")

class Car(Vehicle):
    ''' def __init__() is car class constructor'''
    def __init__(self, name, manufacturer, color, year):
        print ("Creating a car")
        super().__init__(name,manufacturer, color)
        self.year = 2018
        self.wheels = 4
    
        print ("A new car has been created. Name:",self.name)
        print("It has",self.wheels, "wheels")
        print ("The car was built in",self.year)

    def change_gear(self,gear_name):
        print(self.name, "is changing gear to", gear_name)

    def turn(self, direction):
        print (self.name, "is turning", direction)
    

if __name__ == "__main__":

    c = Car("Mustang 5.0 GT Coupe", "Ford","RED",2012)
    print (c.name,c.year,c.wheels)
    
    '''
    v = Vehicle("Softail Delux", "Harley-Davidson", "BLUE")
    c.turn("right")
    v.turn("left")
'''
    #c.drive()
    #c.brake()
    #c. change_gear('P')
'''
    v1 = Vehicle("Fusion 110 EX", "Walton","Black")
    v2 = Vehicle("softtail Delux","Harley-Davidson","Blue")
    v3 = Vehicle("Mustang 5.0 GT Coupe", "Ford","Red")

    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn("left")
    v2.turn("Right")

    v1.brake()
    v2.brake()
    v3.brake()
'''
