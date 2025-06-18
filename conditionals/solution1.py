age_input= (int(input("enter age: ")))
if age_input <13:
    print ("child")

elif 19>age_input>13:
    print("teenage")

elif 59>age_input>19:
    print("adult")

elif 59<age_input<60:
    print("senior")

else:
    print("invalid")

