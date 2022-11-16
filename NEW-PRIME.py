#Prime Numbers

#please write a program that print the first N prime numbers
#N should be declared as a variable at the beginning of your code
#you can hand it in as a link to your file at github or you can attach a file here in the assignment

#3points

#Tanja Grieshaber
#ID: 120685

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

