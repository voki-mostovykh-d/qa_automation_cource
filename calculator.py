import re

# Функции под каждую доступную операцию
def add(a, b=None):
    if b is None:
        if hasattr(a, '__iter__'): # Проверем первый аргумет итерируемый или нет
            return sum(a)
        else:
            return None
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Словарь операций
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Функция для расчета
def calculate_expression():
    while True:
        expression = input("Введите математическое выражение (например, 1.2+3) или одно число: ")

        # Если ввели выражение целиком
        match = re.fullmatch(r'^(\d+(\.\d+)?)([+\-*/])(\d+(\.\d+)?)$', expression)
        if match:
            num1, _, operator, num2, _ = match.groups()
            num1, num2 = float(num1), float(num2)
        else:
            # Если ввели одно число
            if re.fullmatch(r'\d+(\.\d+)?', expression):
                num1 = float(expression)
            else:
                print("Ошибка: неверный формат ввода. Попробуйте снова.")
                continue

            # Ждём оператор
            operator = input("Введите оператор (+, -, *, /): ")
            if operator not in operations:
                print("Ошибка: неверный формат ввода. Попробуйте снова.")
                continue

            # Ждём второе число
            num2_input = input("Введите второе число: ")
            if re.fullmatch(r'\d+(\.\d+)?', num2_input):
                num2 = float(num2_input)
            else:
                print("Ошибка: неверный формат ввода. Попробуйте снова.")
                continue

        result = operations[operator](num1, num2)
        print(f"Результат: {result}")
        break

calculate_expression()