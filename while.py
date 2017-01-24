number = 23
running = True
while running:
    guess = int(input('Введите целое число'))

    if guess == number:
        print('Поздравляю вы победили')
        running = False
    elif guess < number:
        print('Число немного больше этого')
    else:
        print('Число меньше заданного')
else:
    print('Цикл While - завершен')

print("""Завершение программы
Парам-пам -пам
     Тадам!""")

