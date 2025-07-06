class Car ():
        def __init__(self,brand,model):
                
            self.brand =brand
            self.model =model

        def full_name(self):
            return f"{self.brand} {self.model}"

        def fuel_type(self):
            return "deisel or petrol"


class ElectricCar ():
        def __init__(self,E_brand,E_model):
                
            self.user_brand =E_brand
            self.user_model =E_model

        def full_name(self):
            return f"{self.E_brand} {self.E_model}"
    
        def fuel_type(self):
            return "electricity"
        
user_input=input("enter type of vehicle: ")

if user_input=="normal car":
    print(Car(input("enter the brand name: "),input("enter the model: "),input("enter fuel type")))
    print(user_input.brand)
    print(user_input.model)  
    print(user_input.full_name())
    print(user_input.fuel_type())
