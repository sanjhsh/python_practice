max_limit=int(input("enter length of the string: "))
user_input=input("enter a string: ")
i=max_limit

for elements in range(max_limit):
    i-=1
    print(user_input[i])
    