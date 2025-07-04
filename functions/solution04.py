def cal_cir(radius):
    pi=3.1415929

    circumference=2*pi*radius
    area=pi*radius*radius
    print(circumference)
    print(area)

radius=float (input("enter the radius: "))
print(f"circumference and area of a circle is:") 
cal_cir(radius)

