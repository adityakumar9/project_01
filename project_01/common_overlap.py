# List overlap
a = [1, 2, 3, 4, 5, 9, 11, 13, 12, 15, 19, 18, 25, 22, 45, 68, 57, 55, 46]
b = [1, 2, 3, 4, 8, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 25, 28, 29, 54, 45, 75, 57, 56, 65, 58, 85]
c = []

class overLape:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self ):
        if len(self.a) > len(self.b):
            print("A is grater then B")
        elif len(self.b) > len(self.a):
            print("B is grater then A")
        else:
            print("Both are same ")

    def commonList(self):
        for i in self.a:
            if i in self.b:
                c.append(i)

Olap = overLape(a,b)
Olap.compare()
Olap.commonList()
print(c)



