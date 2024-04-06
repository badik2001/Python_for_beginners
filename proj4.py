def encrypt_text():
    print('Hello, this program can encrypt your text')
    step = int(input('Enter a step of cipher(number)'))
    text = list(str(input('Enter a text')))
    new_text = []

    english = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ENGLISH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    russian = ["а","б","в","г","д","е","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    RUSSIAN = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    for i in range(len(text)):

        
        if text[i] in english:
            new_text.append(english[(english.index(text[i]) + step) % 26])
        elif text[i] in ENGLISH:
            new_text.append(ENGLISH[(ENGLISH.index(text[i]) + step) % 26])
        elif text[i] in russian:
            new_text.append(russian[(russian.index(text[i]) + step) % 32])
        elif text[i] in RUSSIAN:
            new_text.append(RUSSIAN[(RUSSIAN.index(text[i]) + step) % 32])
    print(*new_text)
encrypt_text()