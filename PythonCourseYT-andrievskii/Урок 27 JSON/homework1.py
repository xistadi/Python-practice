import json

def get_lovelynumber():
    """Получаем любимое число"""
    filename = "lovelynumber.json"
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def output_lovelynumber():
    """вывод/запись"""
    number = get_lovelynumber()
    if number:
        print("Я знаю ваше любимое число! Это " + str(number))
    else:
        number = input("Введите ваше любимое число: ")
        filename = "lovelynumber.json"
        with open(filename, "w") as f:
            json.dump(number, f)
            print("Мы запомним ваше любимое число " + str(number) + "!")

output_lovelynumber()


