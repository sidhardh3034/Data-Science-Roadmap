# Question 1 Addition

# x=lambda x,y:x+y
# print(x(20,30))    # 50

# Question 2  Multiplication
# x=lambda x,y:x*y
# print(x(5,6))    #30

# Question 3 — Lambda with Condition

# x=lambda x: 'Even' if x%2==0 else "Odd"
# print(x(9))    #Odd

# Question 4 — map() + Lambda
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * 2, numbers))   #[2,4,6,8,10]
# print(result)

# Question 5 - map() + Lambda
# numbers = [1, 2, 3, 4, 5, 6]
# result = list(filter(lambda x: x % 2 == 0, numbers))   #[2, 4, 6]
# print(result)


# Question 6 — filter() + Lambda

# numbers = [10, 15, 20, 25, 30]
# result = list(filter(lambda x: x > 20, numbers))     #[25, 30]
# print(result)

# Question 7 — reduce() + Lambda

from functools import reduce
# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, numbers)    # 10
# print(result)

# Question 8 — reduce() + Lambda
# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x * y, numbers)    # 24
# print(result)



