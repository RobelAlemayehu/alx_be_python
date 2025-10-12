
class Calculator:
    """A class to demonstrate class methods and static methods."""

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
