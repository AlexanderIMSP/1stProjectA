number = 23
guess = int(input('Введите целое число : '))
if guess == number:
    print('Поздравляю, вы угадали, ') #Новый блок
    print(' (Хотя и не выиграли никакого приза!)')
elif guess < number:
    print('Нет, число больше этого')
    print('Попробуйте прибавить к числу', number - guess)
else:
    print('Нет, число меньше заданного. Попробуйте вычесть', guess-number)
print('Programm finished')
