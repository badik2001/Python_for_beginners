import random


def generate_password():
    digits = list("0123456789")
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    punctuation = list("!#$%&*+-=?@^_")
    chair = []
    print(lowercase_letters)

    numbers = input("Включать цифры?; д = да, н = нет")
    if numbers == "д":
        chair += digits
    elif numbers == "н":
        print("Пароль будет менее надёжным")
    else:
        print('Нужно было вводить либо "д", либо "н", но теперь поздно')
    low_letters = input("Добавить прописные буквы?; д = да, н = нет")
    if low_letters == "д":
        chair += lowercase_letters
    elif low_letters == "н":
        print("Пароль будет менее надёжным")
    else:
        print('Нужно было вводить либо "д", либо "н", но теперь поздно')
    up_letters = input("Добавить заглавные буквы?; д = да, н = нет")
    if up_letters == "д":
        chair += uppercase_letters
    elif up_letters == "н":
        print("Пароль будет менее надёжным")
    else:
        print('Нужно было вводить либо "д", либо "н", но теперь поздно')
    symbols = input("Добавить символы?; д = да, н = нет")
    if symbols == "д":
        chair += punctuation
    elif symbols == "н":
        print("Пароль будет менее надёжным")
    else:
        print('Нужно было вводить либо "д", либо "н", но теперь поздно')
    ambiguous_symbols = input("Исключить неоднозначные символы?; д = да, н = нет")
    if ambiguous_symbols == "д":
        del [i], [l], [L], [o], [O]
    elif ambiguous_symbols == "н":
        print("Пароль будет менее надёжным")
    else:
        print('Нужно было вводить либо "д", либо "н", но теперь поздно')

    cnt = int(input("Введите количество паролей"))
    password = random.sample(chair, int(input("Введите длину пароля")))

    print(*password)


generate_password()
