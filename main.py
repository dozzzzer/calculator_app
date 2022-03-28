import calculator


def ask_name():
    user_name = input("Welcome! \nPlease tell me your name: ")
    return user_name


def greet():
    name = ask_name()
    print("\nHello " + name + "!")
    print("Welcome to the Calculator App. You can use this calculator to add, subtract, multiply or divide two "
          "digits.\nYou can quit the program at "
          "any moment by pressing Ctrl + C. Enjoy!")


try:
    greet()
    calculator.calculation(calculator.select_digit_one(), calculator.operation_select(), calculator.select_digit_two())

except KeyboardInterrupt:
    print ("\nYou have terminated the execution. Goodbye!")
