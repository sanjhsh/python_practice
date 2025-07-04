user_input=input("enter the coffee size: ")
ex_input =input("do you want extra shot of espresso: ")
if user_input=="small":
    if ex_input=="yes":
        print("order size is small ","+","extra shot of espresso")

    elif ex_input=="no":
        print("order size is small with no extra shot of espresso")

    else:
        print("invalid input")

elif user_input=="medium":
    if ex_input=="yes":
        print("order size is medium ","+","extra shot of espresso")

    elif ex_input=="no":
        print("order size is medium with no extra shot of espresso")

    else:
        print("invalid input")  

elif user_input=="large":
    if ex_input=="yes":
        print("order size is large ","+","extra shot of espresso")

    elif ex_input=="no":
        print("order size is large with no extra shot of espresso")

    else:
        print("invalid input") 

else:
    print("invalid input")