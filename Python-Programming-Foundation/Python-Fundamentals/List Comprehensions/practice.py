# Practice 1: Create numbers from 1 to 5

x = [i for i in range(1, 6)]
print(x)


# Practice 2: Multiply each number by 10

l = [1, 2, 3, 4, 5]

x = [i * 10 for i in l]
print(x)


# Practice 3: Even numbers

x = [i for i in range(1, 11) if i % 2 == 0]
print(x)


# Practice 4: Odd numbers

x = [i for i in range(1, 10) if i % 2 != 0]
print(x)


# Practice 5: Squares of even numbers

k = [1, 2, 3, 4, 5, 6]

x = [i ** 2 for i in k if i % 2 == 0]
print(x)


# Practice 6: First letter of every word

words = ["python", "data", "science", "machine"]

x = [i[0] for i in words]
print(x)


# Practice 7: Names starting with 'a'

names = ["amal", "arjun", "binu", "arun", "deepak"]

x = [i for i in names if i[0] == 'a']
print(x)


# Practice 8: Cubes from 1 to 5

x = [i ** 3 for i in range(1, 6)]
print(x)


# Practice 9: Even or Odd

x = ['Even' if i % 2 == 0 else 'Odd' for i in range(1, 11)]
print(x)