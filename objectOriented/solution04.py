class Car():
    def __init__(self,brand,model):
        self.__private_attribute=brand
        self.model=model

    def get_private(self):
        return self.__private_attribute
    
user_input=input("do you want to access brand name?: ")

if user_input=="yes":

    my_car=Car(input("enter model:"),input("enter the brand name: "))
    print(my_car.get_private())
    print(my_car.model)
    
elif user_input=="no":
    my_car=Car(input("enter model:"),input("enter the brand name: "))
    print(my_car.model)

else:
    print("invalid input")