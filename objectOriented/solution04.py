class Car():
    def __init__(self,model,brand):
        
        self.__private_attribute=brand 
        self.model=model
        

    def get_private(self):
        return self.__private_attribute
    
    
    
user_input=input("do you want to access brand name?: ")

if user_input=="yes":

    my_car=Car(input("enter model:"),input("enter the brand name: "))
    
    print(my_car.model)
    print(my_car.get_private())
    


elif user_input=="no":
    my_car=Car(input("enter model:"),input("enter the brand name: "))
    
    print(my_car.model)

else:
    print("invalid input")


my_car=Car("tata","safari")
my_car=Car("tata","nexon")
print(my_car._Car
    __private_attribute)
print(my_car.model) 