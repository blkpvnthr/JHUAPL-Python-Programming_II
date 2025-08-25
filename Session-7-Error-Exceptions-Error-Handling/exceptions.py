"""Example of Error Exceptions

When raising a new exception while another exception is already being handled, the new exception’s context attribute is automatically set to the handled exception. 
An exception may be handled when an exception or final clause, or a with statement, is used. Three attributes on exception objects provide information about the context in which the exception was raised:

Try It! Exceptions

Write a Python function named safe_divide that takes two arguments, numerator and denominator, and returns the result of the division. 
The function should handle the ZeroDivisionError exception and return float('inf') if the denominator is zero.
Additionally, it should handle TypeError if either input is not a number and return a string: 'Invalid input: both arguments must be numbers.'

"""

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("[!] Cannot divide by zero.")
except ValueError:
    print("[!] Invalid input: both arguments must be numbers.")
