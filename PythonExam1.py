#Addtion 
def addition (a, b):
    sum = a + b
    return sum

#Subtraction
def subtraction (a, b):
    if a > b:
        difference = a - b
    elif b > a:
        difference = b - a
    return difference

#Multiplication
def multiplication (a, b):
    product = a * b
    return product

#Division
def division (a, b):
    quotient = a / b
    return quotient

#RESULTS
def arithmetic_operations():
    num1 = input("Enter 1st number: ")
    num2 = input("Enter 2nd number: ")

    choice = input("Choose the results you want to see: \n1. Sum \n2. Difference \n3. Product \n4. Quotient\n")
    
    if choice == 1:
        print(addition(num1, num2))
        
    elif choice == 2:
        print(subtraction(num1, num2))

    elif choice == 3: 
        print(multiplication(num1, num2))

    elif choice == 4: 
        print(division(num1, num2))

    else:
        print("Invalid Input")

arithmetic_operations()