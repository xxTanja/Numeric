l1 = [2525, 12536, 585895, 27848]
print(l1[1])
print(l1[1:3])

for i in range(len(l1)):
    print(f'el {i}={l1[i]}')

for val in l1:
    print(f'val={val}')

l1.append(2636)
print(l1)
l1.insert(1, 525623453)
print(l1)
l1.remove(27848)
print(l1)
l1.pop(1)
print(l1)
l1.sort()
l1.sort(reverse=True)
print(l1)


l2 = [2525, 12536, 585895, 'Hello Python 3', 27848]
#TODO Please extract the word "Python" from l2
my_elem = l2[3]
print(my_elem)
print(my_elem[6:12])

#TODO Sum up all numbers in l2
# print('--------------')
# l2.remove('Hello Python 3')
# print(l2)
# #my_elem1=l2
# sum = sum(l2)
# print(sum)

print('--------------')
total_sum = 0
for item in l2:
    if type(item) is int:
        total_sum = total_sum + item
print(total_sum)
print(l2)

#l3 = [ x for x in l2 if type(x)==int]
l3 = [ x for x in l2 if isinstance(x, (int, float, complex))]
print(l3)
print(sum(l3))


print('------------------------------')

#solution from dude in class

l4 = [321,26,23163, 'Hello from Python 3', 3267,89]

sum_of_numbers = 0
for i in range(len(l4)):
    if type(l4[i])==int:
        sum_of_numbers += l4[i]

python_string_index = l4[3].find("Python")
python_string = l4[3][python_string_index:python_string_index+6]
print(sum_of_numbers, python_string)

print('------------------------')

l5 = [x for x in l4 if isinstance(x,(int, float, complex))]
# means same list = x for x l4
#delete string element
print(l4)
print(l5)
print(sum(l5))
#sum of list print(sum(listname))


l6 = [x*3 for x in l5]
#triple the values in l5 *3

print(l6)