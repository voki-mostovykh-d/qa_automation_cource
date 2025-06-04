from basic_calc_module import NewCalc
import re


def calculate_expression():
    calculator = NewCalc()
    while True:
        expression = input(
            "Введите математическое выражение целиком (например, 1.2+3) или число c оператором для работы с памятью (+5, *2): \n")

        # Если ввели выражение целиком
        match_expression = re.fullmatch(r'^(\d+(\.\d+)?)([+\-*/])(\d+(\.\d+)?)$', expression)
        if match_expression:
            num1, _, operator, num2, _ = match_expression.groups()
            num1, num2 = float(num1), float(num2)
            result = calculator.operations[operator](num1, num2)
            if result is not None:
                print(f"Результат: {result}, Память: {calculator.memo_top}")
        else:

            # Если ввели одно число (используем память)
            match = re.fullmatch(r'^([+\-*/])(\d+(\.\d+)?)$', expression)
            if match:
                operator, num, _ = match.groups()
                num = float(num)
                result = calculator.operations[operator](num)
                if result is None:
                    print("Ошибка: память пуста.")
                else:
                    print(f"Результат: {result}, Память: {calculator.memo_top}")


if __name__ == "__main__":
    calculate_expression()
