Program 1: Print 1 to N

n=int(input("Enter Num:"))
for i in range(1,n+1):
    print(i)

#  OUTPUT---------

Enter Num:5
1
2
3
4
5

Program 2: Print N to 1

n=int(input("Enter Num:"))
for i in range(n,0,-1):
    print(i)


#  OUTPUT---------

Enter Num:5
5
4
3
2
1

Program 3: Sum of First N Numbers

n=int(input("Enter Num:"))
s=0
for i in range(1,n+1):
    s+=i
print("Sum: ",s)


#  OUTPUT---------

Enter Num:5
Sum:  15

Program 4: Multiplication Table

n=int(input("Enter Num:"))
for i in range(1,11):
    s=n*i
    print(n,"*",i,"=",s)
    
#  OUTPUT---------
Enter Num:5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

Program 5: Factorial

n=int(input("Enter Num:"))
f=1
for i in range(1,n+1):
    f=f*i
    
print(f)

#  OUTPUT---------

Enter Num:5
120
