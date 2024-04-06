def encrypt_text():
    print('Hello, this program can encrypt your text')
    step = int(input('Enter a step of cipher(number)'))
    direction = input('Enter direction cipher = c, decipher = d')
    text = input('Enter a text').split()
    new_text = []
    new_text2 = []

    english = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ENGLISH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    russian = ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    RUSSIAN = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    
    for word in text:
        
        for i in range(len(word)):

            if word[i] in english:
                if direction == 'c':
                    new_text.append(english[(english.index(word[i]) + step) % 26])
                elif direction == 'd':
                    new_text.append(english[(english.index(word[i]) - step ) % 26])
            elif word[i] in ENGLISH:
                if direction == 'c':
                    new_text.append(ENGLISH[(ENGLISH.index(word[i]) + step) % 26])
                elif direction == 'd':
                    new_text.append(ENGLISH[(ENGLISH.index(word[i]) - step) % 26])
            elif word[i] in russian:
                if direction == 'c':
                    new_text.append(russian[(russian.index(word[i]) + step) % 32])
                elif direction == 'd':
                    new_text.append(russian[(russian.index(word[i]) - step) % 32])
            elif word[i] in RUSSIAN:
                if direction == 'c':
                    new_text.append(RUSSIAN[(RUSSIAN.index(word[i]) + step) % 32])
                elif direction == 'd':
                    new_text.append(RUSSIAN[(RUSSIAN.index(word[i]) - step) % 32])
            elif word[i] in ',.-!&?"':
                new_text.append(word[i])
        new_text2.append(''.join(new_text))
        new_text = []
    print(*new_text2)
encrypt_text()