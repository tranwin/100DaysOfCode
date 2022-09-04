from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

method = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator():
    print(logo)

    num1 = float(input("Please ener the first number: "))
    for symbol in method:
        print(symbol)
    should_continue = True

    while should_continue:
        method_symbol = input("Please enter a method: ")
        num2 = float(input("Please ener the next number: "))
        calculation_func = method[method_symbol]
        result = calculation_func(num1, num2)
        print(f"{num1} {method_symbol} {num2} = {result}")

        continue_cal = input("Type 'y' if you want to continue. Otherwise type 'n'.\n")
        if continue_cal == "y":
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()
         




