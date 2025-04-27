# Определяю класс BasicCalc c его методами (функции расчета из старого калькулятора) и атрибутами (словарь операций)
class BasicCalc:

    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    @staticmethod # Каждый метод делаю статическим с помощью декоратора, без использвания параметра self
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
        self._memory_stack = []
        self.operations.update({ # Обновляю словарь operations, чтобы NewCalc мог использовать свои обновленные функции
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            'mp': self.memo_plus,
            'mm': self.memo_minus,
            'mtop': self._memo_top
        })

    def add(self, a, b=None):
        if b is None:
            if not self._memory_stack:
                return None
            result = BasicCalc.add(self._memory_stack[-1], a)
        else:
            result = BasicCalc.add(a, b)
        if result is not None:
            self.memo_plus(result)
        return result

    def subtract(self, a, b=None):
        if b is None:
            if not self._memory_stack:
                return None
            result = BasicCalc.subtract(self._memory_stack[-1], a)
        else:
            result = BasicCalc.subtract(a, b)
        if result is not None:
            self.memo_plus(result)
        return result

    def multiply(self, a, b=None):
        if b is None:
            if not self._memory_stack:
                return None
            result = BasicCalc.multiply(self._memory_stack[-1], a)
        else:
            result = BasicCalc.multiply(a, b)
        if result is not None:
            self.memo_plus(result)
        return result

    def divide(self, a, b=None):
        if b is None:
            if not self._memory_stack:
                return None
            result = BasicCalc.divide(self._memory_stack[-1], a)
        else:
            result = BasicCalc.divide(a, b)
        if result is not None:
            self.memo_plus(result)
        return result

    def memo_plus(self, value):
        if len(self._memory_stack) < self.memory_size:
            self._memory_stack.append(value)
            return True
        else:
            return None

    def memo_minus(self):
        if self._memory_stack:
            return self._memory_stack.pop()
        else:
            return None

    @property
    def memo_top(self):
        if self._memory_stack:
            return self._memory_stack[-1]
        return None

    def _memo_top(self):  # Внутренний метод для вызова через 'mtop' в operations
        return self.memo_top