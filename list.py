l1 = [323, 234, 23, 2343, 234, 56]

print(l1)
print(l1[1])
print(l1[1:4])

print(l1[-4:])
#print - 4 means last 4 elements

l1.append(765)
#add element to liss

l1.insert(3, 878)
#add element to a speicifc position

l1.remove(26)
#remove element

for i in range(len(l1)):
    print(f'el {i}={l1[i]}')


