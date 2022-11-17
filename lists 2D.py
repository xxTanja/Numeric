l1 = [[1, 6, 7],
      [8, 9, 3],
      [7, 6, 2]]

print(l1)
#representation of matrix
l1_0 = l1[0]
l1_1 = l1[1]
l1_2 = l1[2]

print(l1_1[2])
print(l1[1][2])
#search for the 3 in the list, this si just a matrix

print('-----------------')

#TODO sum rows in l1
print(sum(l1_0))
print(sum(l1_1))
print(sum(l1_2))

# OR
print('-----------------')

for i in range(len(l1)):
    print(sum(l1[i]))

print('-----------------')


#TODO sum columns in l1
#print(sum (l1[0][1]), (l1[1][1]), (l1[2][1]))

#print(sum(l1_0[1] + l1_1[1]) + l1_2[1])
#print(sum(l1_0[1] + l1_1[1]) + l1_2[1])

res = [sum(idx) for idx in zip(*l1)]
print(res)

print('-----------------')

#TODO sum all elements of l1
#print(sum(l1[0]), sum(l1[1]), sum(l1[2]))
#print(sum([0:8]))

print('--------------')

#for item in l1:
 #   if type(item) is int:
  #      total_sum = total_sum + item
#print(total_sum)


print(sum(res))
#sum up results
