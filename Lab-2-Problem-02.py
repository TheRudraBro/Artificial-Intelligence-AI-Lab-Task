list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6,7,8,9]
for x in list2:
    if x not in list1:
        list1.append(x)
print(list1)
        
