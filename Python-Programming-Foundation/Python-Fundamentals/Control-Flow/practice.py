# Prime Number Program

n = int(input("Num: "))

if n <= 1:
    print("Not Prime")
else:
    isprime = True

    for i in range(2, n):
        if n % i == 0:
            isprime = False
            break

    if isprime:
        print("Prime")
    else:
        print("Not Prime")


# Fibonacci Series

n = int(input("Num: "))

n1 = 0
n2 = 1

if n == 0:
    print(n1)
else:
    for i in range(n):
        print(n1, end=" ")
        t = n1 + n2
        n1 = n2
        n2 = t


# Palindrome

n1 = int(input("Num: "))
n = str(n1)

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not")


# Armstrong Number

n = input("Num: ")

temp = int(n)
org = temp
k = 0
s = len(n)

while temp > 0:
    d = temp % 10
    temp //= 10
    k += d ** s

if k == org:
    print("Armstrong")
else:
    print("Not")