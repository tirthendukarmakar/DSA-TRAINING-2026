list=[0,1,4,0,2,5]
for i in list:
    if i==0:
        list.remove(i)
        list.append(i)

print(list)