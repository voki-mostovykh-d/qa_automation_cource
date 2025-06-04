# Определяю класс BasicCalc c его методами (функции расчета из старого калькулятора) и атрибутами (словарь операций)
class BasicCalc:

    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    # Каждый метод делаю статическим с помощью декоратора, без использвания параметра self
    @staticmethod
    def add(a, b=None):
        if b is None:
            if hasattr(a, '__iter__'):
                return sum(a)
            else:
                return None
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


# Создаю класс-наследник BasicCalc
class NewCalc(BasicCalc):
    memory_size = 3

    def __init__(self):
        super().__init__()
        self.memory_stack = []

    # Упрощенные арифметические методы т.к есть универсальный метод для работы с памятью
    def add(self, a, b=None):
        return self._perform_operation(super().add, a, b)

    def subtract(self, a, b=None):
        return self._perform_operation(super().subtract, a, b)

    def multiply(self, a, b=None):
        return self._perform_operation(super().multiply, a, b)

    def divide(self, a, b=None):
        return self._perform_operation(super().divide, a, b)

    def memo_plus(self, value):
        if len(self.memory_stack) < self.memory_size:
            self.memory_stack.append(value)
        else:
            print(f"Ошибка: память заполнена (максимум {self.memory_size}).")
        return value

    def memo_minus(self):
        if self.memory_stack:
            return self.memory_stack.pop()
        else:
            raise ValueError("Ошибка: память пуста.")

    @property
    def memo_top(self):
        if self.memory_stack:
            return self.memory_stack[-1]
        return None

    # Универсальный метод для вычеслений с памятью
    def _perform_operation(self, operation, a, b):
        if b is None:
            b = self.memo_minus()
        return self.memo_plus(operation(a, b))
