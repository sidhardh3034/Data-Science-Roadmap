# Error Handling

Error handling is used to handle errors that occur while a program is running.

## try

The try block contains code that may cause an exception.

Example:

try:
    print(10 / 0)

## except

The except block handles the exception.

Example:

try:
    print(10 / 0)
except:
    print("Error handled")

## Specific Exception

We can handle a particular type of exception.

Example:

try:
    n = int("abc")
except ValueError:
    print("Invalid number")

## Multiple except

Different exceptions can be handled separately.

Example:

try:
    n = int(input("Num: "))
    print(10 / n)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

## else

The else block runs when no exception occurs.

Example:

try:
    n = int("10")
except ValueError:
    print("Invalid")
else:
    print("Valid number")

## finally

The finally block always executes whether an exception occurs or not.

Example:

try:
    print(10 / 2)
except:
    print("Error")
finally:
    print("Done")

## Exception

Exception can be used to catch general exceptions.

Example:

try:
    print(10 / 0)
except Exception:
    print("Something went wrong")

## Common Exceptions

ValueError
- Invalid value or conversion

TypeError
- Operation performed on incompatible data types

ZeroDivisionError
- Division by zero

IndexError
- Index does not exist

KeyError
- Dictionary key does not exist

## raise

The raise keyword is used to manually raise an exception.

Example:

age = 15

if age < 18:
    raise ValueError("Under age")