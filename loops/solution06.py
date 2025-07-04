user_input=int(input("enter the number: "))

factorial=factorial1=1

if user_input<0:
    print(1)

elif user_input==1:
    print(1)

elif user_input>1:
    while factorial1<user_input :
        factorial1+=1
        factorial=(factorial1*factorial)

    print(factorial)

else:
    print("invalid input")