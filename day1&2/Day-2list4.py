# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],
#      [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]

# for i in range(0,6):
#     print(arr[i], end=" ")

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     # FIX: Changed 'kiwi' to 'Kiwi' to match the capitalization above
#     if ls[1] == 'Kiwi': 
#         sum += 20
        
# print(sum)

# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)


mylist=[]
N=int(input("Enter the value of N :"))
for i in range(N):
    val=int(input("Enter the value: "))
    mylist.append(val)
print(mylist)
