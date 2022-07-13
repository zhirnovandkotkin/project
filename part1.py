from random import randint
import math

def human_guess():
    lower = int(input("Введите нижнюю границу:- "))
    upper = int(input("Введите верхнюю границу:- "))

    x = randint(lower, upper)
    print("\n\tУ тебя всего лишь ",
          round(math.log(upper - lower + 1, 2)),
          " три попытки, чтобы угадать число!\n")

    count = 0

    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Твоя догадка:- "))
        if x == guess:
            print("Поздравляю! Число угадано за ",
                  count, " попытки(ок)")
            break
        elif x > guess:
            print("Загаданное число больше твоего!")
        elif x < guess:
            print("Загаданное число меньше твоего!")

    if count >= math.log(upper - lower + 1, 2):
        print("\nЗагаданное число: %d" % x)
        print("\tПопробуй в следующий раз!")
