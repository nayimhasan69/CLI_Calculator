print("Welcome to CLI clculator !")
def calculator():
    print("Select oparation")
    print("1. Add")
    print("2. Sudtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    try:
        c=int(input("Enter choice(1/2/3/4/5):"))
        if c==1:
            add()
        elif c==2:
            sub()
        elif c==3:
            mul()
        elif c==4:
            div()
        elif c==5:
            exit
        else:
            print("Invalid input !")
            calculator()
    except ValueError:
        print("Invalid Input")
        calculator()
def add():
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    print(a,"+",b,"=",a+b)
    calculator()
def sub():
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    print(a,"-",b,"=",a-b)
    calculator()
def mul():
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    print(a,"*",b,"=",a*b)
    calculator()
def div():
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    if b==0:
        print("Error! Division by zero.")
    else:
        print(a,"/",b,"=",a/b)
    calculator()
calculator()
