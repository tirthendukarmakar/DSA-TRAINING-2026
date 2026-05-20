a=int(input("Enter marks1: "))
b=int(input("Enter marks2: "))
c=int(input("Enter marks3: "))

gender=input("Enter sex: ")

per=(a+b+c)/3

if a>=35 and b>=35 and c>=35:
    print("Passed")

    if per>=65 and gender=="Male":
        print("Eligible for placement")
    else:
        print("Not eligible")
    
else:
    print("Fail")