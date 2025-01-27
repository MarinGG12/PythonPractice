#Print from 1 to 100
n = 0
for n in range(1, 100):

    #Mutiples of both three (3) and five (5) prints "FizzBuzz"
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    
    #Multiples of three (3) print "Fizz"
    elif n % 3 == 0: 
        print("Fizz")
    
    #Multiples of five (5) prints "Buzz"
    elif n % 5 == 0:
        print("Buzz") 
    
    else:
        print(n)
    