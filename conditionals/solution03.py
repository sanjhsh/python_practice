grade_input=int(input(("enter marks: ")))
if 90<grade_input<100:
    print("A")

elif 80<grade_input<91:
    print("B")

elif 70<grade_input<81:
    print("C")

elif 60<grade_input<71:
    print("D")

elif 61> grade_input:
    print("F")

else:
    print("invalid input")