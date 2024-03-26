from random import *
n = random.randint(1, 100)
print('Добро пожаловать вчисловую угадайку')

def is_valid(number):
    if 1 <= int(number) <= 100:
        return True
    return False

for i in range(5):
    user_number = input()
    if is_valid(user_number) == True:
        user_number = int(user_number)
    else:
        print('А может введём всё-таки целое число от 1 до 100')
        print('У тебя осталось', 4 - i, 'попыток')

if user_number < n:
    print('Ваше число меньше загаданного, попробуйте ещё разок')
elif user_number > n:
    print('Ваше число больше загаданного, попробуйте ещё разок')
elif user_number == n:
    print("Вы угадали поздравляем")

print('Спасибо что играли в числовую угадайку, ещё увидимся ...')