name = "divisao"

def execute(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b