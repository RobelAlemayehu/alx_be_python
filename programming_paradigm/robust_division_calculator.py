

def safe_divide(numerator, denominator):
    
    try:
       value = float(numerator) / float(denominator)
       return value
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")    
    
        