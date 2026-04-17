def safe_divide():
    try:
        num1 = float(input("Enter the first num: "))
        num2 = float(input("Enter the second num: "))
        result = num1 / num2
        print(f"The result is: {result}")

    except ValueError:
        print("Wrong one, dear! Enter a number, not text")
        
    except ZeroDivisionError:
        print("Sorry, black hole generation is not a supported feature. I handle arithmetic, not spacetime singularities!")

safe_divide()