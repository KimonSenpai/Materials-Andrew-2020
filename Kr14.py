FILE = "27-B_2.txt"

f = open(FILE, 'r')

n = int(f.readline())

m1, m2, m7, m14 = 0, 0, 0, 0
mp = 0

for i in range(n):
    val = int(f.readline())

    if val % 14 == 0:
        mp = max(mp, val*m1, val*m2, val*m7, val*m14)
        m14 = max(m14, val)
    elif val % 7 == 0:
        mp = max(mp, val*m2, val*m14)
        m7 = max(m7, val)
    elif val % 2 == 0:
        mp = max(mp, val*m7, val*m14)
        m2 = max(m2, val)
    else:
        mp = max(mp, val*m14)
        m1 = max(m1, val)

print(mp)




