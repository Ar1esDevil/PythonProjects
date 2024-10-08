import random

a = [
    "ножницы:бумага",
    "бумага:камень",
    "камень:ящерица",
    "ящерица:спок",
    "спок:ножницы",
    "ножницы:ящерица",
    "ящерица:бумага",
    "бумага:спок",
    "спок:камень",
    "камень:ножницы"
]

choices = ["камень", "ножницы", "бумага", "ящерица", "спок"]

def game():

    print('Вы запустили игру "Камень, ножницы, бумага, ящерица, спок"')

    while True:

        b = input("(выберите камень, ножницы, бумагу, ящицу или спок): ").lower()
        if b not in choices:
            print("Неверный ввод. Пожалуйста, выберите одно из пяти действий.")
            continue

        c = random.choice(choices)  
        print(f"Компьютер выбрал: {c}")        

        if b == c:
            print("Ничья!")
            continue
        
        for match in a:
            i, j = match.split(':')
            if b == i and c == j:
                print("Вы победили!")
                break
            elif c == i and b == j:
                print("Победил Компьютер!")
                break

if __name__ == "__main__":
    game()
