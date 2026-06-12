Q1 Even or Odd
n=int(input("NUM: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

#  OUTPUT--------

NUM: 8
Even


Q2 Positive or Negative
n=int(input("NUM: "))
if n>=0:
    print("Positive")
else:
    print("Negative")

#  OUTPUT--------

NUM: -5
Negative

Q3 Largest of Two Numbers
n1=int(input("NUM1: "))
n2=int(input("NUM2: "))

if n1>n2:
    print("Largest ",n1)
else:
    print("Largest ",n2)


#  OUTPUT--------


NUM1: 10
NUM2: 20
Largest  20

Q4 Eligible to Vote

age=int(input("Age: "))
if age>=18:
    print("Eligible")
else:
    print("Not")

#  OUTPUT--------

Age: 17
Not


Q5 Grade Calculator

Rules:

90+ => A
75+ => B
50+ => C
Below 50 => Fail

m=int(input("Mark: "))
if m>=90:
    print("A")
elif m>=75:
    print("B")
elif m>=50:
    print("C")
else:
    print("Fail")

#  OUTPUT--------


Mark: 52
C