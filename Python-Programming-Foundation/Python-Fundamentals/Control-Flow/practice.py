# Prime Number Program

# n=int(input("Num: "))
# isprime=True
# if n <= 1:
#     print("Not Prime")
# else:
#     isprime = True
# for i in range(2,n):
#     if n%i==0:
#         isprime=False
#         break
        
# if isprime:
#     print(" Prime")
# else:
#     print("NotPrime")

#    OUTPUT---------------------

# Num: 7
#  Prime
# Num: 9
# NotPrime


n=int(input("Num"))
n1=0
n2=1
if n==0:
    print(n1)
else:
    for i in range(n):
        print(n1,end=" ")
        t=n1+n2
        n1=n2
        n2=t

