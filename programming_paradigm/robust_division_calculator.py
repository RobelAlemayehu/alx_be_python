

def safe_divide(self,numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
    
    try:
       value = float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Denominator can not be zero")
    except ValueError:
        print("Value can not be non numeric character")    
    
        