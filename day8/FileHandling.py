import csv
f = open("student.csv",'a')
a = csv.writer(f)
studId=int(input("Enter id: "))
Studename=input("ENter name: ")
phy=int(input("Enter phy marks: "))
chem=int(input("Enter chem marks: "))
math=int(input("Enter maths marks: "))
total=phy+chem+math
percentage=total/3
a.writerow([studId,Studename,phy,chem,math,total,percentage])
print("File has created")
