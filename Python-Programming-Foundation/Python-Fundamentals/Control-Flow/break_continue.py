# BREAK EXAMPLE

print("Break Example")

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Output:
# 1
# 2
# 3


print("\nContinue Example")

# CONTINUE EXAMPLE

for i in range(1, 6):
    if i == 4:
        continue
    print(i)

# Output:
# 1
# 2
# 3
# 5