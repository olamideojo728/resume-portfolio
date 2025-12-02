# Simple Calculator Demo
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error" if b == 0 else a / b

if __name__ == "__main__":
    print("Demo Calculator")
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
