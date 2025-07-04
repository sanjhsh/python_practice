array_1= ["banana","mango","papaya"]
array_2=["cheery","apple","strawberry"]
user_input_1= input("enter name of the fruit: ")

if user_input_1 in array_1:
    
    user_input_2=input("enter colour of the fruit: ")

    if user_input_2=="yellow":
        print("ripe")

    elif user_input_2=="green":
        print("unripe")

    elif user_input_2=="brown":
        print("overripe")

    else:
        print("invalid input")

elif user_input_1 in array_2:
    
    user_input_2=input("enter colour of the fruit: ")

    if user_input_2=="red":
        print("ripe")

    elif user_input_2=="green":
        print("unripe")

    elif user_input_2=="brown":
        print("overripe")

    else:
        print("invalid input")

else:
    print("invalid input")
