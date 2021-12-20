def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
def d(n, b):
    d.t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r = ''
    while n:
        n, y = divmod(n, b)
        r = d.t[y]+r
    return r

password = []
s = input()
for i in range(len(s)):
    x = int(''.join(string2bits(s[i]))) + 100000000
    x = int(str(x), 2)
    password.append(x//10%10)
    a = x
    while a >= 36:
        a = a//(i+2)
    password.append(a)
    c = d(x,a)
    password.append(c)
    x -= 256
    n = ""
    r = 2
    while x > 0:
        y = str(x % r)
        n = y + n
        x = int(x / r)
        r = r + 1
    password.append(len(c))
    password.append('Z')
print(*password, sep='')