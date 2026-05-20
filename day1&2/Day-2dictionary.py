# mydict={
#     101: "prashant",
#     102: "ashish",
#     "103": "mohini",
#     "104": "trivani",
#     101: "ashish",
#     104:"ashish"
# }
# print(mydict)

# a = mydict[102]
# print(a)

# mydict[102]="peter"
# print(mydict)

# for x in mydict:
#     print(x)

# for x in mydict.values():
#     print(x)

# for x,y in mydict.items():
#     print(x,y)

#adding a new key:value pair
# mydict["mobile_no"]= 4646463738
# print(mydict)

# ...mydict
# mydict.pop(101)
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a={'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# print(arr)
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)

# my_dict={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4
# # print(my_dict)
# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)

# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum)
# print(my_dict)

# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# box['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))

# dict={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# rec={"Name":"Python","Age":"20"}
# r=rec.copy()
# print(id(r)==id(rec))
# print(id(r))
# print(id(rec))

# rec={"Name":"Python","Age":"20","Addr":"NJ","Country":"USA"}
# id1=id(rec)
# del rec
# rec={"Name":"Python","Age":"20","Addr":"NJ","Country":"USA"}
# id2=id(rec)
# print(id1==id2)

#Sample Input:{"A":50,"B":30,"C":70}
#Expected Output:"C"

#Sample Input:{"X":20,"Y":10,"Z":30}
#Expected Output:"Y"
# a={"X":50,"Y":30,"Z":70}
# min_key = min(a,key=a.get)
# print(min_key)

#A function to count the frequency of elements in a alist using a dictionary
#Sample Input=[1,2,2,3,4,3,5]
#Expected Output={"1":1,"2":2,"3":2,"4":1,"5":1}

# num=123
# a=num%10
# num=num//10
# b=num%10
# c=num//10
# rev=a*100+b*10+c*1
# print(rev)

# num=123456
# sum=0
# while(num!=0):
#     r=num%10
#     sum=sum*10+r
#     num=num//10

# print(sum)



Amount=int(input("Please enter amount for withdraw : "))
print(" 100 notes= ",Amount//100)
print(" 50 notes= ",(Amount % 100)//50)
print(" 20 notes= ",((Amount % 100)%50)//20)
print(" 10 notes= ",(((Amount % 100) % 50) % 20 ) % 10)
print(" 5 notes= ",((((Amount % 100) % 50) % 20 ) % 10) //5)
