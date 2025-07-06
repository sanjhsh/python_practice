class Car():
    car_count=0

    def __init__(self,model,brand):
        
        self.__private_attribute=brand
        self.model=model
        Car.car_count+=1

    def get_private(self):
        return self.__private_attribute
    
    @staticmethod
    def general_dis():
        return "cars are the mewns of transport"
    
my_car=Car("tata","safari")
my_car=Car("tata","nexon")


print(Car.car_count)

print(my_car.general_dis())
print(Car.general_dis())

