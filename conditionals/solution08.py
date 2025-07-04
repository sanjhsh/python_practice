user_input= (input("enter the password: "))

if len(user_input)<6:
    print("weak password")

elif 6<len(user_input)<10:
    print("medium password")

elif 11<len(user_input):
    print("strong password")

else:
    print("invalid input")
