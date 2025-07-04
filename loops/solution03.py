user_input=int(input("enter the number: "))
multiplication=0

for i in range(1,11):
    multiplication+=1
    if multiplication==5:
        continue
    print(user_input,"x",multiplication,"=",user_input*multiplication)
    