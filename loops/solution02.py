user_input=int(input("enter the range: "))
division= user_input
sum=0

if user_input%2==0:
    while division>0:
        sum=(division)+(division-2)
        division-=2
    print(sum)

elif user_input%2!=0:
    for i in range ((division-1)/2):
        sum=(user_input-1)+(user_input-3)
        user_input-=3
    print(sum)

else:
    print("invalid input")