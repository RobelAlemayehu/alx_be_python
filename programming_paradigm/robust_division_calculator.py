

def safe_divide(numerator, denominator):
    
    try:
       result = float(numerator) / float(denominator)
       return f"The result of the dvision is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."    
    
        