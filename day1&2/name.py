# name="prashant"
# newname=""
# for i in name:
#     if i not in newname:
#         newname+=i

# print(newname)
# print((newname))

# name="prashant"
# s=len(name)
# newname=""
# for i in range(s-1,-1,-1):
#     newname+=name[i]
# print(newname)

# s=input("Enter string: ")
# if (s==s[::-1]):
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# vowels=['a','e','i','o','u']
# name="hello"
# cons=0
# vow=0
# for i in name:
#     if i in vowels:
#         vow+=1
#     else:
#         cons+=1
# print("consonent= ",cons)
# print("vowels= ",vow)


# a="listen"
# b="silent"
# anagram tech  is checking same charectors in both strings

a="hello world"
count=0
subc=0
for i in a:
    subc+=1
    if i=="":
        count+=1
        subc=0

if subc!=0:
    print(count+1)
else:
    print(count)