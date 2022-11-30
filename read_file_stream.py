my_file = 'hello.txt'

with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    while line:=f.readline():
        i += 1
        print(f'{i}: {line}', end='')