def mul_arg(array):
    array=[]
    sum=0
    

    for i in range(user_input1):
        user_input2= int(input("enter a number: "))
    
        array.append(user_input2)
    print(array)

    for i in range(user_input1):
        sum+=array[i]
    print(sum)
user_input1= int(input("enter range of numbers: "))

mul_arg(user_input1)
