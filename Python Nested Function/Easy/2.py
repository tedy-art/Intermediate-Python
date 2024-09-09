"""
Create a function calculator() that defines an inner function to add two numbers,
then returns the sum.
"""


def Calculator(x=0, y=0):
    def sum_inner():
        print(f"The sum of {x} and {y} is: {x + y}.")

    return sum_inner()


Calculator(15, 32)
Calculator(10, 20)
Calculator(6, 5)
Calculator(7)
