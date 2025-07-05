class ElectricCar():
    def __init__(self,brand ,model,battery_size):
        self.brand= brand
        self.model= model
        self.battery_size=battery_size
    
my_car= ElectricCar(input("enter the brand name: "),input("enter the model: "),input("enter battery size: "))
print(my_car.brand)
print(my_car.model)  
print(my_car.battery_size)

