print('Hello, this program can convert a number to any number system')
convert = input('if you want to convert in decade system, enter "10", binary "2", octal "8", hexadecimal "16"')
number = input('Enter number')
if convert == "2":
    print(bin(int(number))[2:], 'binary number system')
if convert == "8":
    print(oct(int(number))[2:], 'octal number system')
if convert == "16":
    print(hex(int(number))[2:].upper(), 'hexadecimal number system')
if convert == "10":
    number_system = int(input("Enter number's system"))
    print(int(number, number_system))