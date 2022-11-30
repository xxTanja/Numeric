d1 = {'Jan': 'January', 'Feb': 'Feburaray', 'Mar': 'March'}
print(d1)

d1 = {'Jan': 'January', 'Feb': 'Feburaray', 'Mar': 'March', 'Jan': 'Enero'}
print(d1)

print(d1['Feb'])

d1['Apr'] ='April'
print(d1)

d1['Apr'] ='Aprilo'
print(d1)

for v in d1.values():
    print(f'{v}')
#print single values of the dictornary

print('-------------')

t1 = (2344, 234)
t11, t12 = t1
print(t11)

for k, v in d1.items():
    print(f'{k}:{v}')