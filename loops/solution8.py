user_input=int(input("enter the number: "))

if user_input<0:
    print("invalid input")

elif user_input==1:
    print(user_input," is not a prime number")

elif 1<user_input<9:
    if user_input%2==0:
        print(user_input," is not a prime number")

    elif user_input%2!=0:
        print(user_input," is a prime number")

elif user_input>9:
    for i in range(2,8):
        if user_input%i==0:
            print(user_input," is a not prime number")
            break
        else:
            print(user_input," is a prime number")
            break