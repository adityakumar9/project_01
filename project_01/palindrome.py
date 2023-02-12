# Palindrome using class
a =int(input("Enter String or number: "))
print(a)

#print(a[::])
print(a[::-1])

class palindrom:

    def __init__(self, a):
        self.a = a

    def pali(self):
        if self.a[::] == self.a[::-1]:
            print("The input is Palindrome")
        else:
            print("The input is not Palindrome")

Pal = palindrom(a)
Pal.pali()