print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division" )

def add(D):
    A = D[0] + D[1]
    return A

def sub(S):
    B = S[0] - S[1]
    return B

def dev(V):
    C = V[0] / V[1] if V[1] != 0 else "Un-define"
    return C

def mul(M):
    M = M[0] * M[1]
    return M



def Calculator(calc):
    #sid = [float(input("Enter first value ")), float(input("Enter second value "))]
    if calc == 1:
        sid = [float(input("Enter first value ")), float(input("Enter second value "))]
        print(add(sid))

    elif calc == 2:
        sid = [float(input("Enter first value ")), float(input("Enter second value "))]
        print(sub(sid))

    elif calc == 3:
        sid = [float(input("Enter first value ")), float(input("Enter second value "))]
        print(mul(sid))

    elif calc == 4:
        sid = [float(input("Enter first value ")), float(input("Enter second value "))]
        print(dev(sid))
    else:
        print("Please press correct number! Number is invalid: ")
    return calc


print(Calculator(int(input("Enter the value: "))))
