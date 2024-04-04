def encrypt_text():
    print('Hello, this program can encrypt your text')
    direction = ('Enter direction cipher = c, decipher = d')
    alfabet = input('Enter alfabet English = e, Russian = r')
    step = int(input('Enter a step of cipher(number)'))
    text = list(input('Enter a text'))
    new_text = []
    if direction == 'c':
        if alfabet == 'e':
            for i in text:
                if str(text[i]).islower():
                    new_text.append(chr(ord(text[[i]]) + (ord(text[[i]]) + step) % 122))
                elif str(text[i]).isupper():
                    new_text.append(chr(ord(text[[i]]) + (ord(text[[i]]) + step) % 90))
        elif alfabet == 'r':
            for i in text:
                if str(text[i]).islower():
                    new_text.append(chr(ord(text[[i]]) + (ord(text[[i]]) + step) % 255))
                elif str(text[i]).isupper():
                    new_text.append(chr(ord(text[[i]]) + (ord(text[[i]]) + step) % 233))
    elif direction == 'd':
        if alfabet == 'e':
            for i in text:
                if str(text[i]).islower():
                    new_text.append(chr(ord(text[[i]]) - (ord(text[[i]]) + step) % 122))
                elif str(text[i]).isupper():
                    new_text.append(chr(ord(text[[i]]) - (ord(text[[i]]) + step) % 90))
        elif alfabet == 'r':
            for i in text:
                if str(text[i]).islower():
                    new_text.append(chr(ord(text[[i]]) - (ord(text[[i]]) + step) % 255))
                elif str(text[i]).isupper():
                    new_text.append(chr(ord(text[[i]]) - (ord(text[[i]]) + step) % 233))
    print(new_text)

encrypt_text()