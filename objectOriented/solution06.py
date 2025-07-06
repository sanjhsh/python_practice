class Car():
    car_count=0

    def __init__(self,model,brand):
        
        self.__private_attribute=brand
        self.model=model
        Car.car_count+=1

    def get_private(self):
        return self.__private_attribute
    
my_car=Car("tata","safari")
my_car=Car("tata","nexon")


print(Car.car_count)

