def bits2string(b=None):
    return ''.join([chr(int(l, 2)) for l in b])
def d(n, b):
    d.t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r=''
    while n:
        n, y = divmod(n, b)
        r=d.t[y]+r
    return r
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
print(*o, sep='')