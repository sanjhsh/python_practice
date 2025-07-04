default_name="shakti"

def greet_func(name):
    
    print(f"hello {name} nice to meet you")

user_input=input("enter your name: ")

user_type=print(type(user_input))
if user_input=="":
    greet_func(default_name)
    

else:
    greet_func(user_input)
