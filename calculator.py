from basic_calc_module import NewCalc
import re

def calculate_expression():
    calculator = NewCalc()
    while True:
        expression = input("Введите математическое выражение (например, 1.2+3) или число c оператором (+5, *2). \n"
                           "Доп. функции: mp <число> - чтобы добавить в память, mm - удалить, mtop - вывести значение на вершине памяти.\n:")

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
                    print("Ошибка: память пуста. Для сохранения в память используйте 'mp <число>")
                else:
                    print(f"Результат: {result}, Память: {calculator.memo_top}")
            else:

                # Команды для работы с памятью
                match_memo = re.fullmatch(r'^(mp|mm|mtop)\s*(\d+(\.\d+)?)?$', expression)
                if match_memo:
                    command = match_memo.group(1)
                    value_str = match_memo.group(2)

                    if command == 'mp':
                        if value_str:
                            value = float(value_str)
                            if calculator.memo_plus(value) is None:
                                print(f"Ошибка: память заполнена (максимальное значение {calculator.memory_size}).")
                            else:
                                print(f"Значение {value} добавлено в память. Текущая память: {calculator.memo_top}")
                        else:
                            print("Ошибка: для 'mp' необходимо указать значение.")
                    elif command == 'mm':
                        deleted_value = calculator.memo_minus()
                        if deleted_value is None:
                            print("Ошибка: память пуста. Для сохранения в память используйте 'mp <число>")
                        else:
                            print(f"Значение {deleted_value} удалено из памяти.")
                    elif command == 'mtop':
                        top_value = calculator.memo_top
                        if top_value is None:
                            print("Память пуста. Для сохранения в память используйте 'mp <число> ")
                        else:
                            print(f"Значение на вершине памяти: {calculator.memo_top}")

                # Если ввели просто число (можно положить в память)
                elif re.fullmatch(r'\d+(\.\d+)?$', expression):
                    print("Для сохранения в память используйте 'mp <число>'.")
                else:
                    print("Ошибка: неверный формат ввода. Попробуйте снова.")

if __name__ == "__main__":
    calculate_expression()