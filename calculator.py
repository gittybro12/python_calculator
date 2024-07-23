def Add(num1,num2):
    return num1 + num2

def Subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

functions = {
    '+' : Add,
    '-' : Subtract,
    '*' : multiply,
    '/' : divide

} 
def calculator():
    num1 = float(input("what is the first number? "))
    for x in functions.keys():
        print(f'{x}')
    operation = input("Enter the operation you want to perform ")
    num2 = float(input("what is the second number? "))

    operation_symbol = functions[operation]
    run = operation_symbol(num1=num1,num2=num2)


    print(f"{num1} {operation} {num2} = {run}")

    still_in = True
    while still_in:
        cont = input(f"Type 'y' to continue calculating with {run} or 'no' to start a new calculation: ")

        if cont == 'no':
            still_in = False 
            calculator()
        else:    
            operation = input("pick another operation? ")
            num3 = float(input("Enter a number? "))
            operation_symbol = functions[operation]
            run2 = operation_symbol(run,num3)

            print(f"{run} {operation} {num3} = {run2}")
calculator()
