day_input=str(input("enter day: "))
age_input=int(input("enter age: "))

if day_input=="wednesday":
    if age_input>=18:
        print("movie ticket price", "= $12","-","discount price "," = $ 2"," = $10")

    elif age_input<18:
        print("movie ticket price", "= $8","-","discount price "," = $ 2"," = $6")

    else:
        print("invalid input")

else:
    if age_input>=18:
        print("movie ticket price = $12")

    elif age_input<18:
        print("movie ticket price = $8")

    else:
        print("invalid input")