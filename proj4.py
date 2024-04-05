def encrypt_text():
    print('Hello, this program can encrypt your text')
    direction = input('Enter direction cipher = cip, decipher = dec')
    alfabet = input('Enter alfabet English = e, Russian = r')
    step = int(input('Enter a step of cipher(number)'))
    text = list(str(input('Enter a text')))
    new_text = []
    if direction == 'cip':
        if alfabet == 'e':
            for c in text:
                if c.islower():
                    new_text.append(chr(ord(c) + step))
                elif c.isupper():
                    new_text.append(chr(ord(c) + step))
        elif alfabet == 'r':
            for c in text:
                if c.islower():
                    print(ord(c))
                    new_text.append(chr((ord(c) + step) % 1071))
                    
                elif c.isupper():
                    print(ord(c))
                    new_text.append(chr((ord(c) + step) % 1071))
                    print(ord(c))
    elif direction == 'dec':
        if alfabet == 'e':
            for c in text:
                if c.islower():
                    new_text.append(chr(ord(c) + step))
                    
                elif c.isupper():
                    new_text.append(chr(ord(c) + step))
        elif alfabet == 'r':
            for c in text:
                if c.islower():
                    new_text.append(chr(ord(c) + step))
                elif c.isupper():
                    new_text.append(chr(ord(c) + step))
    print(''.join(new_text))

encrypt_text()