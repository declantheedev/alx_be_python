num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));
operation = input("Choose the operation (+, -, *, /):").strip().lower();
match operation:
    case '+':
        result = num1 + num2;
        print('The result is {}'.format(result));
    case '-':
        result = num1 - num2;
        print("The result is {}".format(result));
    case '*':
        result = num1 * num2;
        print("The result is {}".format(result));
    case '/':
        if float(num2) != 0:
            result = num1 / num2;
            print("The result is {}".format(result));
        else:
            print("Error: Division by zero is not allowed.");