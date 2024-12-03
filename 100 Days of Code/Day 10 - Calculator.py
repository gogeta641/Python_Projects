from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


number1 = float(input("What's the first number?  "))

continue_working = True

while continue_working:
    operator1 = input("Pick an operation: \n+ \n- \n* \n/ \n")
    number2 = float(input("What's the next number?  "))
    result = (operations[operator1](number1, number2))
    print(f"{number1} {operator1} {number2} = {result}")
    user_continue_working = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
    if user_continue_working == "y":
        number1 = result
    else:
        number1 = float(input("What's the first number?  "))