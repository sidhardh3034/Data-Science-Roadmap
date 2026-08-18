# Practice 1: Handle Division by Zero

try:
    n = int(input("Num: "))
    print(100 / n)
except ZeroDivisionError:
    print("Cannot divide by zero")


# Practice 2: Handle Invalid Input

try:
    n = int(input("Num: "))
    print(n)
except ValueError:
    print("Invalid input")


# Practice 3: Handle Multiple Exceptions

try:
    n = int(input("Num: "))
    print(100 / n)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")


# Practice 4: Handle IndexError

try:
    x = [10, 20, 30]
    print(x[5])
except IndexError:
    print("Index out of range")


# Practice 5: Handle KeyError

try:
    d = {"name": "Sidhardh"}
    print(d["age"])
except KeyError:
    print("Key not found")


# Practice 6: Handle TypeError

try:
    x = "10" + 5
    print(x)
except TypeError:
    print("Type error")


# Practice 7: Raise ValueError

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Eligible"

try:
    print(check_age(16))
except ValueError:
    print("Invalid age")