import random
n = random.randint(1, 100)
print('Добро пожаловать вчисловую угадайку, введите число от 1 до 100')
print('Введите число от 1 до 100')
print('у вас 7 попыток')

def is_valid(number):
    if 1 <= int(number) <= 100:
        return True
    return False

for i in range(7):
    user_number = input()
    if is_valid(user_number) == True:
        user_number = int(user_number)
        if user_number < n:
            print('Ваше число меньше загаданного, попробуйте ещё разок')
            print('У тебя осталось', 6 - i, 'попыток')
        elif user_number > n:
            print('Ваше число больше загаданного, попробуйте ещё разок')
            print('У тебя осталось', 6 - i, 'попыток')
        elif user_number == n:
            print("Вы угадали поздравляем")
            break
    else:
        print('А может введём всё-таки целое число от 1 до 100')
        print('У тебя осталось', 6 - i, 'попыток')

print('Спасибо что играли в числовую угадайку, ещё увидимся ...')