import logic
from decouple import config


while True:
    total = int(config("MY_MONEY"))

    while total > 0:
        your_sum = int(input("Введите вашу ставку: "))

        if your_sum > total:
            print(f"Ваша сумма {total}, пожалуйста уменьшите.")
            continue

        your_number = int(input("Угадайте число: "))

        if your_number == logic.win_number:
            total += your_sum * 2
            print(f"Вы победили! {your_sum * 2}")
        if your_number > 31:
            print('Загадывайте от 1 до 31')
            continue
        else:
            total -= your_sum
            print("Вы проиграли :(")

        play_again = input("Хотите сыграть еще? (Да/Нет): ").capitalize()

        if play_again == "Да":
            continue
        elif play_again == "Нет":
            print(f"Ваша сумма: {total}")
            total = 0
            break
        else:
            print("Invalid Error. Yes or No?")
            continue

    if total <= 0:
        print("Игра окончена!")
        break