#conditions

p = True
q = False

if p:
  print('p is True')

else:
   print('p is not True')


print('--------')

if not p:
  print('p is not True')

else:
   print('p is True')


print('--------')
#end operator is only true if both are true otherwise it is false
if p and q:
  print('p and q are True')

else:
     print('p and q are not True')

print('--------')
#end operator is false only if both are false otherwise it if true
if p or q:
 print('p or q are True')

else:
     print('p or q are not True')

print('--------')
#the endoperator is only true is one is true otherwise it is false
if p ^ q:
 print('p xor q are True')

else:
     print('p xor q are not True')

print('--------')

#object orientation
#none is a an empty pointer/string = no value
#every VAR has a value
# none means we created a pointer but not created an object, so nothing we can reference it with

v = None
if v:
   print(f'v={v}')
else:
  print('not v')

t = 5
print (t)


#None can not be calculated by an equation
# will be an error --> tt = t + v
# you can use an addition equation for two strings, however, you can not use a "NONE" type for an addition


#print (tt)

print('----')
#works with both int & float, it doesnt matter, if/else function can erkennen both types

w = 10.99
print(type(w))
z = 11
print(type(z))
if w >= z:
 print('w >=z')
else:
 print('not w >= z')

#double == means we assign a value to another VAR
#what does != means??
if w == z:
 print('w = z')
else:
 print('w != z')

 print(z)
 print(w)

print('-------------')

y = 10 if w == 11 else 50
print (f'y={y}')
#print (f'y={}'.format(y)) equviilant = print (f'y={y}')

#we cannot put int and string together, so to be able to do that we need to convert it into a chr()
print('y=' + str(y))
