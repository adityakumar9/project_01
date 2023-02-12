# Palindrome
a = input("Enter a number or string: ")
b = []
c = []
for i in range(len(a)):
    b.append(a[i])
    c.append(a[len(a)-i-1])

print(b)
print(c)

# if b == c:
#     print("The input is Palindrome")
# else:
#     print("The input is not Palindrome")

