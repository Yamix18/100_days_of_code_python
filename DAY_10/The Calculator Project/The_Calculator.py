from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 - n2


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def computer():
    should_accumulate = True
    n1 = float(input("What's the first number?: "))
    while should_accumulate:
        for operator in operations_dict:
            print(operator)
        operations = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        result = operations_dict[operations](n1, n2)
        print(f"{n1} {operations} {n2} = {result}")

        ask_to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") .lower()

        if ask_to_continue == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 100)
            print(logo)
            computer()
print(logo)
computer()


