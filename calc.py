def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def mult(x,y):
    return x*y
def div(x,y):
    if y == 0:
        raise ValueError("Can't divide by zero")
    # FLOOR DIVISION - NO REMAINDER
    return x / y