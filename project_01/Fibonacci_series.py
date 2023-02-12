a = int(input("Enter a Number: "))
b = 0
c = [1]

# 11235

class fibonacci:

    def __init__(self, a):
        self.a = a

    def feboRule(self):
        for i in range(0, self.a):
             b= c[i] + c[i-1]
             c.append(b)
        print(c)

Febo = fibonacci(a)
Febo.feboRule()

