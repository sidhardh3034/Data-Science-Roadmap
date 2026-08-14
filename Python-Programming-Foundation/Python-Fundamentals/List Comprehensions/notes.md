# List Comprehensions

List comprehension is a short way to create a list using a loop.

## Basic Syntax

[expression for item in iterable]

## Basic Example

numbers = [i for i in range(1, 6)]

Output:
[1, 2, 3, 4, 5]

## Expression

squares = [i * i for i in range(1, 6)]

Output:
[1, 4, 9, 16, 25]

## With Condition

even = [i for i in range(1, 11) if i % 2 == 0]

Output:
[2, 4, 6, 8, 10]

## With if-else

result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]

Output:
["Odd", "Even", "Odd", "Even", "Odd"]

## Working with Strings

names = ["amal", "arjun", "arun", "binu"]

result = [name.upper() for name in names]

Output:
["AMAL", "ARJUN", "ARUN", "BINU"]

## String Condition

names = ["amal", "arjun", "binu", "arun"]

result = [name for name in names if name.startswith("a")]

Output:
["amal", "arjun", "arun"]

## Nested List Comprehension

result = [i * j for i in [1, 2, 3] for j in [1, 2]]

Output:
[1, 2, 2, 4, 3, 6]

## Important Point

List comprehension creates a new list.

The general form is:

[expression for item in iterable]

With a condition:

[expression for item in iterable if condition]

With if-else:

[expression_if_true if condition else expression_if_false for item in iterable]