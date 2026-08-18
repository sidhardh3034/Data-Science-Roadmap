# Question 1  ZeroDivisionError

# try:
#     print(10 / 0)
# except:
#     print("Error handled")   #Error handled

# Question 2 — except with a Specific Exception
# try:
#     n = int("abc")
#     print(n)
# except ValueError:
#     print("Invalid number")  #Invalid number


# Question 3 — Multiple except
# try:
#     n = int(input("Num: "))
#     print(10 / n)

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Cannot divide by zero")  #input is 0  Output:Cannot divide by zero

# Question 4 — else
# try:
#     n = int("10")
# except ValueError:
#     print("Invalid")
# else: 
#     print("Valid number")    #Output:Valid number

# Question 5 — finally
# try:
#     print(10 / 2)
# except:
#     print("Error")
# finally:
#     print("Done")  #Output:5.0  Done

# Question 6 — finally with an Error

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Cannot divide")
# finally:
#     print("Done")    #Output:Cannot divide Done

# Question 7 — Specific Exception
# try:
#     x = int("hello")
# except ValueError:
#     print("Value Error")
# except TypeError:
#     print("Type Error")      #Output:Value Error

# Question 8 — except Exception
# try:
#     x = 10 / 0
# except Exception:
#     print("Something went wrong")   #Output:Something went wrong

# Question 9 — raise
# age = 15

# if age < 18:
#     raise Exception("Not eligible")
# else:
#     print("Eligible")   #Exception: Not eligible.

# Question 10
# try:
#     age = 15

#     if age < 18:
#         raise ValueError("Under age")

# except ValueError:
#     print("Invalid age")      #Output:Invalid age

