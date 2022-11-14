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
