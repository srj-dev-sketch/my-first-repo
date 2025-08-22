list =[1,2,3,4,5,6,8,1,2,3,4,5,6,7,8]
list2=[]

for i in list:
        if i not in list2:
                    list2.append(i)

print(list2)
