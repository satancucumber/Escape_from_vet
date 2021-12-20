def bits2string(b=None):
    return ''.join([chr(int(l, 2)) for l in b])
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
def d(n, b):
    d.t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r=''
    while n:
        n, y = divmod(n, b)
        r=d.t[y]+r
    return r
print('Введите 1, если хотите создать пароль по кодовому слову')
print('Введите любую другую цифру, если хотите восстановить слово из пароля')
p = int(input())
if p == 1:
    password = []
    s = input()
    for i in range(len(s)):
        x = int(''.join(string2bits(s[i]))) + 100000000
        x = int(str(x), 2)
        password.append(x // 10 % 10)
        a = x
        while a >= 36:
            a = a // (i + 2)
        if a < 10:
            password.append(0)
        password.append(a)
        c = d(x, a)
        password.append(c)
        x -= 256
        n = ""
        r = 2
        while x > 0:
            y = str(x % r)
            n = y + n
            x = int(x / r)
            r = r + 1
        password.append(len(n))
        password.append('Z')
    print('Пароль:')
    print(*password, sep='')
else:
    s = input()
    z = []
    o = []
    i = s.find('Z')
    while i != -1:
        a = int(s[1:3])
        x = int(s[3:i-1], a) - 256
        x = d(x, 2)
        s = s[i+1:]
        i = s.find('Z')
        z.append('0'+str(x))
        o.append(bits2string(z))
        z = []
    print('Кодовое слово:')
    print(*o, sep='')