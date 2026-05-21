# try:
#     a = int(input("Enter 1st number: "))
#     b = int(input("Enter 2nd number: "))


#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer value :")
# except ValueError:
#     print("Enter only integer value: ")
# except:
#     print("ABC")


# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)

#     print("Can't divide by zero")
# except ValueError:
#      print("Enter only integer value :")
# finally:
#      print("I always executed")


#logging
# import logging
# logging.basicConfig(filename="newfile,txt",level=logging.DEBUG)
# try:
#     a=int(input("Enter first integer no: "))
#     b=int(input("Enter second integer no: "))
#     print(a/b)
# except (ZeroDivisionError.ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging level is set up.Check 'newfile.txt' for log details.")

#File handling
import csv
f = open("employee.csv",'a')
a = csv.writer(f)
# a.writerow(["EmpID","Emp Name","Emp Age"])
empid=int(input("ENter employee id :"))
empName=input("Enter Employee name")
age  =int(input("Enter employee age :"))
a.writerow([empid,empName,age])
print("File has created")
