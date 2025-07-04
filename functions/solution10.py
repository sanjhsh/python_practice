def rec_fac(num):
    if num==0:
        return 1
    else:
        return num*rec_fac(num-1)
    

user_input=int(input("enter a number: "))
print(rec_fac(user_input))