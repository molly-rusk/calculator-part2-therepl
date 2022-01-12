"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    playerInput = input('>')
    entries = playerInput.split(" ")

    if "x" in entries:
        print("Exiting calculator...")
        break
    elif len(entries) < 2:
        print("More inputs required")
    
    mathSymbol = entries[0]
    num1 = entries[1]

    if len(entries) < 3:
        num2 = "0"

    else:
        num2 = entries[2]

    if len(entries) > 3:
        num3 = entries[3]

    answer = None

    if not num1.isdigit() or not num2.isdigit():
        print("Please enter numbers only to perform operations")

    elif mathSymbol == "+":
        answer = add(float(num1), float(num2))

    elif mathSymbol == "-":
        answer = subtract(float(num1), float(num2))

    elif mathSymbol == "*":
        answer = multiply(float(num1), float(num2))

    elif mathSymbol == "/":
        answer = divide(float(num1), float(num2))

    elif mathSymbol == "square":
        answer = square(float(num1))

    elif mathSymbol == "cube":
        answer = cube(float(num1))

    elif mathSymbol == "pow":
        answer = power(float(num1), float(num2))

    elif mathSymbol == "mod":
        answer = mod(float(num1), float(num2))
        
    else:
        answer = "Please enter an arithmetic symbol followed by two integers."

    print(answer)
