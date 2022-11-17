t1 = (1412, 254346)
t2 = (2, 4, 6, 7)

print(t1[1])
print(t2[3])
#t1[1] = 24 THIS IS NOT POSSIBLE NOT ABLE TO CHANGE

# tupple is unchangeable
# make sure that no one can admit changes
# BUT can create a new one with based on the exisiting one
# unchangeable structure only readible, Good example for big data,
# we dont modify, instead we have a flow to way out, a way of dealing. data is distributed
#simpleer  & nobody by accident will change it

t3 = t2[1:3]
print(t3)

print ('-----------------------')

l4 = [321, 26, 23163, 3267,89, 26, 3267, 89]

print(l4)
s1 = set(l4)
print(s1)
#set is not ordere ITS random
#the sequence is completely random
#duplicates are deleted
#cannot adress an element
#its not subscripatble
#not indexing of a set --> #print(s1[3])
#you can reorder it

for el in s1:
    print(el)

# we can use this code above to use for el to refernece the iterations

l5 = list(s1)
print(l5)
