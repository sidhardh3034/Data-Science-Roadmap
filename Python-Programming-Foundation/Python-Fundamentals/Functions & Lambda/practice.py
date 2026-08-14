# Practice 1: Palindrome

n = input("Num: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Practice 2: Square Function

def square(n):
    return n * n

p = int(input("Num: "))
print(square(p))


# Practice 3: Even Check

def is_even(n):
    return n % 2 == 0

print(is_even(8))


# Practice 4: Lambda Addition

add = lambda a, b: a + b

print(add(10, 20))


# Practice 5: Lambda Multiplication

multiply = lambda a, b: a * b

print(multiply(5, 6))