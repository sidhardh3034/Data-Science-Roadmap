# Functions & Lambda

## Functions

A function is a reusable block of code.

Syntax:

def function_name():
    # code

## Parameters

Parameters are values passed to a function.

Example:

def square(n):
    return n * n

## Return

return sends a value back from the function.

Example:

def add(a, b):
    return a + b

## Local Variable

A variable created inside a function is a local variable.

Example:

x = 10

def test():
    x = 20
    print(x)

test()
print(x)

Output:
20
10

## Global Variable

A variable created outside a function is a global variable.

The global keyword allows us to modify a global variable inside a function.

Example:

x = 10

def test():
    global x
    x = 20

test()
print(x)

Output:
20

## Lambda Functions

A lambda is a small anonymous function.

Syntax:

lambda arguments: expression

Example:

square = lambda x: x * x

## Lambda with Multiple Arguments

add = lambda a, b: a + b

## Conditional Lambda

check = lambda x: "Even" if x % 2 == 0 else "Odd"

## map()

map() applies a function to every element.

Example:

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

Output:
[2, 4, 6, 8, 10]

## filter()

filter() selects elements based on a condition.

Example:

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

Output:
[2, 4, 6]

## reduce()

reduce() combines elements step by step.

Example:

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

Output:
10