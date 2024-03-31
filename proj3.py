import random
def generate_password():
    digits = list('0123456789')
    lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    punctuation = list('!#$%&*+-=?@^_')
    chair = ''
    
    cnt = int(input('Введите количество паролей?; д = да, н = нет'))
    lenght_password = int(input('Введите длину пароля?; д = да, н = нет'))
    numbers = int(input("Включать цифры?; д = да, н = нет"))
    low_letters = input("Добавить прописные буквы?; д = да, н = нет")
    up_letters = input("Добавить заглавные буквы?; д = да, н = нет")
    symbols = input("Добавить символы?; д = да, н = нет")
    ambiguous_symbols = input("Исключить неоднозначные символы?; д = да, н = нет")

    print(lowercase_letters)
generate_password()