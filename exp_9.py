try:
    a = int(input("Enter the number: "))
    result = a / 2
    print(result)
except (ArithmeticError, ValueError):
    print("An error occurred\n")
