class Car ():
        def __init__(self,user_brand,user_model):
                
            self.user_brand =user_brand
            self.user_model =user_model

        def full_name(self):
            return f"{self.user_brand} {self.user_model}"



class ElectricCar(Car):
    def __init__(self,user_brand ,user_model,battery_size):
        super().__init__(user_brand,user_model)
        self.battery_size=battery_size
    
my_car= ElectricCar(input("enter the brand name: "),input("enter the model: "),input("enter battery size: "))
print(my_car.user_brand)
print(my_car.user_model)  
print(my_car.full_name())
print(my_car.battery_size)