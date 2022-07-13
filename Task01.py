# 1- Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это буквы")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Да")
    elif 0 < num < 6:
        print("Нет")
    else:
        print("Напишите число от 1 до 7")


num = InputNumbers("Введите число: ")
checkNumber(num)