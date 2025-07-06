class Car():

    def __init__(self,brand,model):
        self.var1= brand
        self.var2= model

    def fuel_type(self):
        return "petrol or diesel"
        
class ElectricCar():
    def __init__(self,ebrand,emodel):
        self.var3=ebrand
        self.var4=emodel

    def fuel_type(self):
        return "electricity"

car_type=input("enter the type of car: ")

if car_type=="normal car":
    user_input1=Car(input("enter the brand name : "),input("enter the model:"))
    print(user_input1.var1)
    print(user_input1.var2)
    print(user_input1.fuel_type())

elif car_type=="electric car":
    user_input2=ElectricCar(input("enter the brand name : "),input("enter the model:"))
    print(user_input2.var3)
    print(user_input2.var4)
    print(user_input2.fuel_type())

my_car=Car("tata","safari")
my_car=Car("tata","nexon")
print(my_car.__private_attribute)
print(my_car.model) 