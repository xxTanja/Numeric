
#a loop is a way to run a code multiple times
#the simplest thing a range
#range will be start with a 0
#range works until the last of the (XX) and starts with 0
#iteration means the running of this part of code
v = 0
for i in range(5):
    print(f'i={i}')
    v = v + 1
#just a tab-stopp makes a difference in code

print (f'v={v}')

print('--------------')
#range only works with int not with any float numbers

#to start with 1 use range 1 til 5 & it will stop with 4
for i in range (1, 5):
 #   i =5
  print(f'i={i}')

print('--------')

#to start with 9 use reversed range from 10
for i in reversed(range(-5, 10,2)):
  print(f'i={i}')

print('------------')
#while loop why is it different:
# if I put j the VAR smaller than while j = then the loop is infinete and will run forever
# if j is equal to 3 means skip the code below and skip 3
# and go to the next iteration
#break means the loop at a specific point in time here j eqals to 5

#j = 0
#while j < 7:
 #   j += 1
  #  if j ==3:
   #     continue
    #if j == 5:
     #  break
   # print(f'j={j}')

print('-------------')

#while true is a n infinte loop but it can be manually stopped
# we are intentially can stop it inside

# when do we use while loops?
# = until a certain condition is met
# and that condition can be met in different ways,
# either while-true or while jXX


#when do we use full loops?
# = when we know how many iteration we are going to run


while True:
    j += 1
    if j ==3:
        continue
    if j == 5:
       break
    print(f'j={j}')