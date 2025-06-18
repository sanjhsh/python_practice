user_input=int(input("enter the year:" ))

if user_input%400==0:
    if user_input%100==0:
        print(user_input," is leap year")
    

    elif user_input%100!=0:
        print(user_input," is not a leap year")

    elif user_input%4==0:
        if user_input%100==0:
            print(user_input," is leap year")
        elif user_input%100!=0:
            print(user_input," is not a leap year")
        else:
            print("invalid input")

    elif user_input%4!=0:
        print(user_input," is not a leap year")

elif user_input%400!=0:
    if user_input%100!=0:
        print(user_input,"is not a leap year")

    elif user_input%100==0:
        if user_input%4==0:
            print(user_input," is a leap year")
        elif user_input%4!=0:
            print(user_input," is not aleap year")
else:
    print("invalid input")
