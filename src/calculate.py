
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def divide_with_remainder(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    quotient = x // y
    remainder = x % y
    return quotient, remainder

def power(base, exponent):
    return base ** exponent

def compare(x, y):
    if x == y:
        return "equal"
    elif x > y:
        return "greater"
    else:
        return "less"
