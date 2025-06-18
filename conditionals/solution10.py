user_input=input("enter specie of your pet: ")
age_input=int(input("enter age of the pet"))

if user_input=="dog":
    if age_input<0:
        print("invalid input")

    elif 0<age_input<2:
        print("puppy food")

    elif 2<age_input:
        print("senior dog food")

    else:
        print("invalid input")


elif user_input=="cat":
    if age_input<0:
        print("invalid input")

    elif 0<age_input<5:
        print("kitten food")

    elif 6<age_input:
        print("senior cat food")

    else:
        print("invalid input")

else:
    print("invalid input")