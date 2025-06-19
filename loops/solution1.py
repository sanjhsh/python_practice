
list_size= int(input("enter list's size: "))

list=[]
element=0

for i in range (list_size):
    user_input=input("enter list's elements: ")
    list.append(user_input)

print(list)


for elements in list:
    if elements>=0:
        element+=1
print("positive elements of the list are ",element)

