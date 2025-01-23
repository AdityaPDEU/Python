#Largest and smallest value out of three
def q2():
    a=float(input(" enter a:"))
    b=float(input(" enter b:"))
    c=int(input("enter c:"))
    if a>b>c:
        print("largest is a:",a)
        print("b and c are smaller then a")
    elif a<b>c:
        print(" b is larger:",b)
    else:
        print("smaller is c :",c)
q2()
q2()
q2()
