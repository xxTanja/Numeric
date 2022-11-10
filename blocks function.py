
j = 10

def sum(a=2, b=10):
    print(f'j={j}')
    h = 12
    return a + b


c = 5
d = 8

print(f'sum(c,d)={sum(c, d)}')
print(f'sum(c,d)={sum(c)}')
print(f'sum(c,d)={sum()}')
print(f'sum(c,d)={sum(b=42)}')
print(f'h{h}')