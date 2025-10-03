

def safe_divide(self,numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
    
    try:
       value = float(numerator) / float(denominator)
       return value
    except ZeroDivisionError:
        print("Denominator can not be zero")
    except ValueError:
        print("Input must be numeric values")    
    
        