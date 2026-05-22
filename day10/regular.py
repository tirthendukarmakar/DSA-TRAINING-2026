# import re
# count=0
# pattern = re.compile("function")
# #print(pattern)
# matcher = pattern.finditer("A function in python is defined by a def statement,python.The general syntax looks like this;def function-name(Parameter list): i.e,the function body.Thr parameter python list consists of none or more parameters.")

# #print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())

# print("The number of occurances: ",count)



# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")

# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())

# print("The number of occurances: ",count)





# import re
# obj = input("Enter any charector ")
# objmatch=re.finditer(obj,"a7b @k9z")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())




# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.match(a,"python is very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at beginning level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("There is no matching at beginning level")




# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.fullmatch(a,"pythonisvery")
# print(mtch)
# if mtch!=None:
#     print("match found")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("Full match not found")


# import re
# a = input("Enter mail id: ")
# mtch = re.fullmatch(a,"\w[a-zA-Z0-9_.]*@gmail[].com",s)
# if mtch!=None:
#     print("Valid e-mail id")
# else:
#     print("Invalid e-mail id")



# import re

# a = input("Enter mail id: ")

# # The pattern looks for alphanumeric characters/dots/underscores, followed by @gmail.com
# # We escape the dot (\.) so it matches a literal period, not "any character"
# pattern = r"[\w.]+@gmail\.com"

# # Order: re.fullmatch(pattern, string)
# mtch = re.fullmatch(pattern, a)

# if mtch is not None:
#     print("Valid e-mail id")
# else:
#     print("Invalid e-mail id")



# import re

# mo = input("Enter mobile no: ")



# # Order: re.fullmatch(pattern, string)
# obj = re.fullmatch("[0-5]\d{9}",mo)

# if obj != None:
#     print("Valid mobile no")
# else:
#     print("Invalid mobile no")




#Search() function
# import re
# a = input("Enter string to perform match operation :")
# mtch = re.search(a, "python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("there is no matching anywhere")


# import re
# mtch = re.findall('[A-Z]',"abch3hdh5bk72Q$&*")
# print(mtch)



# import re
# mtch = re.sub('[a-z]','*','2345 ABCD habc deff')
# print(mtch)



# import re
# mtch = re.subn('[0-7]','@','ab3gd6nk17')
# print(mtch)
# print("the string is=",mtch[0])
# print("the number of replacement is=",mtch[1])



#write a python program to extract all mpbile input.txt where numbers are mixed with normal

# f1=open("input.txt","r")
# f2=open("output.txt","w")
import re

# The pattern looks for a digit starting with 6-9, followed by exactly 9 more digits
# \b represents a "word boundary" so we don't accidentally pull 10 digits out of a 15-digit serial number
# pattern = r"\b[6-9]\d{9}\b"

# try:
#     # 1. Open and read the text file
#     with open("input.txt", "text", encoding="utf-8") as file:
#         content = file.read()
    
#     # 2. Extract all matching mobile numbers
#     mobile_numbers = re.findall(pattern, content)
    
#     # 3. Display the results
#     if mobile_numbers:
#         print(f"Found {len(mobile_numbers)} mobile number(s):")
#         for num in mobile_numbers:
#             print(num)
#     else:
#         print("No valid mobile numbers found in the file.")

# except FileNotFoundError:
#     print("Error: The file 'input.txt' was not found. Please make sure it's in the same folder as this script.")




# Program to print the number of lines, words and characters
# present in the given file

import os
import sys

fname = input("Enter File Name: ")

if os.path.isfile(fname):
    print("File exists:", fname)
else:
    print("File does not exist:", fname)
    sys.exit(0)

f = open(fname, "r")

lcount = 0
wcount = 0
ccount = 0

for line in f:
    lcount = lcount + 1
    ccount = ccount + len(line)

    words = line.split()
    wcount = wcount + len(words)

f.close()

print("The number of Lines:", lcount)
print("The number of Words:", wcount)
print("The number of Characters:", ccount)
