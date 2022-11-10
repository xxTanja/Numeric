#whenever we have anything of a loop


a = 5

for i in range(4):
    print(f'i={i}')
    print(f'a={a}')
    a = 7
    print(f'a={a}')

print('--------')
for i in range(4):
    print(f'i={i}')
    print(f'a={a}')


c = 1

if a > 6:
    if b < 10:
        d = 463
    else:
        d = 346

print(f'd = {d}')