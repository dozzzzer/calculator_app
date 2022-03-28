import operator


def operation_select():
    operation = input("\nPlease select an operation by typing:\n'+' for addition \n'-' for subtraction \n'*' for "
                      "multiplication  \n'/' for division \n\n")

    if operation == "+":
        print ("You have selected addition")
    elif operation == "-":
        print ("You have selected subtraction")
    elif operation == "*":
        print ("You have selected multiplication")
    elif operation == "/":
        print ("You have selected division")
    else:
        while not (operation == "*" or operation == "-" or operation == "+" or operation == "/"):
            operation = input("\nPlease select a valid operand! Try again: ")

    return operation


def select_digit_one():
    i1 = input("\nPlease type the first digit: ")
    return i1


def select_digit_two():
    i2 = input("\nPlease type the second digit: ")
    return i2


def calculation(input1, operand, input2):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

    if operand == "/" and input2 == "0":
        result = float("0")
    else:
        result = ops[str(operand)](float(input1), float(input2))
    print ("\nThe result is: ", result)
    continuation = input("\nDo you wish to continue? (Y/N): ")
    inputs = \
        {"yes": ["y", "Y"], "no": ["n", "N"]}

    while not (continuation in inputs['yes'] or continuation in inputs['no']):
        continuation = input("\nPlease type a valid answer! (Y/N): ")
    if continuation in inputs['yes']:
        calculation(select_digit_one(), operation_select(), select_digit_two())
    elif continuation in inputs['no']:
        quit()



