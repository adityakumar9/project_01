# Prime Number
a = int(input("Enter a number: "))
b = []

for i in range(2, a):
    for j in range(2,a):
        if i % j == 0:
            break
    if i==j:
        print(i, end=" ")








