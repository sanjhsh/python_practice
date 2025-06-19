user_input=int(input("enter the range: "))
sum=0

if user_input%2==0:
    division_1= int(user_input/2)
    for i in range (division_1):
        sum+=3
    print(sum)

elif user_input%2!=0:
    division_2=int((user_input-1)/2)
    for i in range (division_2):
        sum+=4
    print(sum)

else:
    print("invalid input")