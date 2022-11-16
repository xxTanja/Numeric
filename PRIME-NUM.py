#Prime Numbers

#please write a program that print the first N prime numbers
#N should be declared as a variable at the beginning of your code
#you can hand it in as a link to your file at github or you can attach a file here in the assignment

#3point

n = 50
print(n)

def isPrime(n):
    if (n <= 1):
        return False
    if(n <=3):
        return True
    if(n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (n % i == 0 or n % (i + 2) == 0):
        return False
    i = i + 6
    return True


#check of prime numbers
if(isPrime(11)):
    print("true")
else:
    ("false")

print('-----------------------------------')


num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


print ('-----------')

for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')


print ('-----------------------------')


Number = 1

while (Number <= 100):
    count = 0
    i = 2

    while (i <= Number // 2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number, end='  ')
    Number = Number + 1


print('--------------------------')

N = 100
List_Prime = []

minimum = int(1)
maximum = int(100)

for Number in range (minimum, maximum + 1):
    count = 0
    if i >= 1 and i < 2:
        List_Prime.append(i)
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break
    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

print ('-----------------------------------------')
