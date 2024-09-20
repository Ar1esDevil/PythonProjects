import random

def generate_number():
    secret_number = random.sample(range(10), 4)
    return ''.join(map(str, secret_number))

def bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return bulls, cows

def play_game():
    secret_number = generate_number()
    counter = 0

    print("Добро пожаловать в игру 'Быки и коровы'!")
    print("Загадано 4-ех значное число с уникальными цифрами. Попробуйте его угадать.")

    while True:
        guess = input("Введите ваше предположение (4 уникальные цифры): ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Неверный ввод. Пожалуйста, введите 4-значное число с уникальными цифрами.")
            continue

        counter += 1
        bulls, cows = bulls_and_cows(secret_number, guess)

        print(f"Коровы: {cows}, Быки: {bulls}")

        if cows == 4:
            print(f"Поздравляем! Вы угадали число {secret_number} за {counter} попыток.")
            break

if __name__ == "__main__":
    play_game()