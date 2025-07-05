class Car ():
        def __init__(self,user_brand,user_model):
                
            self.brand =user_brand
            self.model =user_model

        def full_name(self):
            return f"{self.brand} {self.model}"

my_car= Car(input("enter the brand name: "),input("enter the model: "))
print(my_car.brand)
print(my_car.model)       
print(my_car.full_name())