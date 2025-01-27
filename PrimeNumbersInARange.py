#Find all prime numbers within a user-specified range.
#Take two inputs from the user:
start = int(input("Enter Start of range: "))
end = int(input("Enter End of range: "))

num = 0
for num in range(start, end):
    num += 1
    print(num)