word = (input('Введите кодовое слово:')).split()
#буквы в код ASCII
def codeASCII(word):
    for i in range(len(word)):
        word[i] = ord(word[i])
    return word
#номера в двоичную систему (8-ми битная запись)
def tobinarcode(word):
    for i in range(len(word)):
        word[i] = '0' * (8 - len(bin(word[i])[2:])) + bin(word[i])[2:]
    return word
#реверс
def revers(word):
    word = str(word)
    word = word[::-1]