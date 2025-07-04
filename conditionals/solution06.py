user_input=int(input("enter the distance in km:"))

if user_input<3:
    print("walk")

elif 3<=user_input<15:
    print("bike")

elif 15<user_input:
    print("car")

else:
    print("invalid input")