"""
child 1,2,3... [...]
Each next child says a whole number (integer) starting from 0
If the number can be divided by 3, print "Fizz"
If the number can be divided by 5 , print "Buzz"
If the number can be divided by 3 and 5, print "Fizz Buzz"

"""

number = 0

print("Welcome to FizzBuzz\n")

for number in range (100):
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        print("Fizz Buzz: " +str(number))
    elif int(number % 3) == 0:
        print("Fizz: " + str(number))
    elif int(number) % 5 == 0:
        print("Buzz: " + str(number))
    else:
        print(number)
    
    number=number+1



#ulepszenie z wpisywaniem i sprawdzaniem