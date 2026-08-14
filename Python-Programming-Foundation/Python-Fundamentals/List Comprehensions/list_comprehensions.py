# Basic List Comprehension

# numbers = [i for i in range(1, 6)]   # [1, 2, 3, 4, 5]
# print(numbers)


# Question 1
# x=[i for i in range(5)]  #[0, 1, 2, 3, 4]
# print(x)

# Question 2
# x = [i * 2 for i in range(1, 6)]   #[2, 4, 6, 8, 10]
# print(x)    


# Question 3 — Condition
# x = [i for i in range(1, 11) if i % 2 == 0]  #[2, 4, 6, 8, 10]
# print(x)

# Question 4 — Squares with Condition
# x = [i * i for i in range(1, 11) if i % 2 == 0]   #[4, 16, 36, 64, 100]
# print(x)

# Question 5 — Odd Numbers
# x=[i for i in range(1,10) if i%2!=0]  #[1, 3, 5, 7, 9]
# print(x)

# Question 6 — Strings
# names = ["amal", "arjun", "arun", "binu"]
# x = [name.upper() for name in names]        # ["AMAL", "ARJUN", "ARUN", "BINU"]
# print(x)

# Question 7 — Condition with Strings
# names = ["amal", "arjun", "arun", "binu"]
# x = [name for name in names if name.startswith("a")]   #["amal", "arjun", "arun"]
# print(x)

# Question 8 — if...else
# numbers = [1, 2, 3, 4, 5]
# x = ["Even" if i % 2 == 0 else "Odd" for i in numbers]  #["Odd", "Even", "Odd", "Even", "Odd"]
# print(x)

# Question 9 — Nested List
# x = [i + j for i in [1, 2] for j in [10, 20]]  #[11, 21, 12, 22]
# print(x)


# Question 8 — List Comprehension with Strings
# words = ["python", "data", "science"]
# x = [len(word) for word in words]   #[6, 4, 7]
# print(x)

# Question 9 — Numbers
# l=[1, 2, 3, 4, 5]
# x=[i*10 for i in l]
# print(x)

# Question 10 — Filter + Calculation
# k = [1, 2, 3, 4, 5, 6]
# x = [i**2 for i in k if i % 2 == 0]    #[4, 16, 36]
# print(x)   


# Question 11
# words = ["python", "data", "science", "machine"]
# x=[i[0] for i in words]
# print(x)                 #["p", "d", "s", "m"]

# Question 12 — Condition + String
# names = ["amal", "arjun", "binu", "arun", "deepak"]
# k=[i  for i in names if i[0]=='a']
# print(k)                         #["amal", "arjun", "arun"]


# Question 13 — Numbers

# print(list(i**3 for i in range(1,6)))   #[1, 8, 27, 64, 125]


# Question 14 — Conditional Expression

# x=['Even' if i%2==0 else 'Odd' for i in range(1,11)]   
# print(x)    #['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


