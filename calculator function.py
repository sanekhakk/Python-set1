num1=int(input("num1: "))
2num2=int(input("num2: "))

def simplecalc(a,b=100):
    s=a+b
    d=a-b
    m=a*b
    print("addition:",a)
    print("subtraction:".d)
    print("multiplication:",m)

simplecalc(a=num1)
simplecalc(b=num2, a=num1)


