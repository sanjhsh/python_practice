list_size=int(input("enter list's size: "))

list=[]
element=0

for i in range (list_size):
    user_input=str(input("enter list's elements: "))
    list.append((user_input))

print(list)

for i in list:
    if list.count(i)==2:
        print(i)
        break
    else:
        print("no duplicate found")
        break