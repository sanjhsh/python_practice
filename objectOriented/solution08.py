class Car():
    def __init__(self,model,brand):
        
        self.__private_attribute=brand
        
        self.__model=model
        

    def get_private(self):
        return self.__private_attribute
    
    @property
    def get_model(self):
        return self.__model
    
my_car=Car("tata","safari")
my_car.get_model()=="car"

print(my_car.get_model())
    

    
    
