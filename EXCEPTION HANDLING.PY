def divisor(a, b):
    """Returns the remainder when a is divided by b"""
    return a % b

try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = divisor(num1, num2)
    print(f"Result: {result}")
    
except ValueError:
    print("Please enter only integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Thank you")

