def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    if(b == 0 ):
        print("Eror!, Divsion by zero")
    return a/b

def mod(a,b):
    if(b == 0 ):
        print("Eror!, Divsion by zero")
    return a%b

print ("Select Opertion ")
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")
print("5. MOD")

while True:

    choice = input("Entre choice :")

    if  choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number :" ))
        num2 = float(input("Enter Second number :"))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1 , num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1 , num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1 , num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {div(num1 , num2)}")

        elif choice == '5':
            print(f"{num1} % {num2} = {mod(num1 , num2)}")

        else:
            print('Invalid input! , please select valid option .')

        next_calculation = input("Do you want to perform another calculation ? (yes/no:)")
        if next_calculation.lower()!= 'yes':
            break