#Prime Numbers

#please write a program that print the first N prime numbers
#N should be declared as a variable at the beginning of your code
#you can hand it in as a link to your file at github or you can attach a file here in the assignment

#3points

N = 100
List_Prime = []

minimum = int(1)
maximum = int(100)

for Number in range (minimum, maximum + 1):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break
    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

print ('-----------------------------------------')
