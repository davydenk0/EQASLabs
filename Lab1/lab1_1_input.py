class Calculator:
    def calculate(self, a, b, operation):
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b != 0:
                result = a / b
            else:
                result = None
        else:
            result = None
        return result