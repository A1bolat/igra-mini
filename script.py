def read_choice(prompt, allowed):
    while True:
        choice = input(prompt).strip()
        if choice in allowed:
            return choice
        print("Неверный ввод! Выберите из списка.")


def read_guess():
    while True:
        num = input("Введите число (1-50): ").strip()
        if num.isdigit() and 1 <= int(num) <= 50:
            return int(num)
        print("Ошибка! Нужно число от 1 до 50.")


def compare_guess(guess, secret):
    if secret > guess:
        return "больше"
    elif secret < guess:
        return "меньше"
    return "угадал"


def show_attempts(left):
    print(f"Осталось попыток: {left}")


def show_rules():
    print("\n--- ПРАВИЛА ---")
    print("Загадано число от 1 до 50. У вас 6 попыток.")
    print("Ошибки ввода (буквы, числа не от 1 до 50) попытку не тратят.\n")


def play_game():
    secret = 27
    attempts = 6

    while attempts > 0:
        show_attempts(attempts)
        guess = read_guess()
        res = compare_guess(guess, secret)

        if res == "угадал":
            print("Победа! Вы угадали число!\n")
            return

        attempts -= 1
        print(f"Загаданное число {res}, чем {guess}.\n")

    print(f"Вы проиграли! Загаданное число было: {secret}\n")


def main():
    while True:
        print("=== МЕНЮ ===")
        print("1 - Начать")
        print("2 - Правила")
        print("0 - Выход")

        choice = read_choice("Ваш выбор: ", ["0", "1", "2"])

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Выход из игры.")
            break


if __name__ == "__main__":
    main()