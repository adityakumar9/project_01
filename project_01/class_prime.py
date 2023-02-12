#  Prime number using class

a = int(input(("Enter Range: ")))

class prime:
     def __init__(self, a):
         self.a = a

     def prime_df(self):
         for i in range(2, self.a):
             if i > 1:
                 for j in range(2, i):
                     if (i%j) == 0:
                         break
                 else:
                     print(i, end=",")
Prim= prime(a)
Prim.prime_df()

