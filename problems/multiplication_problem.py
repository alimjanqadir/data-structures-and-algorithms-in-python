def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z += y
        x -= 1
    return z


def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1: z +=y
        x = x >> 1
        y = y << 1
    return z

def russian_rec(a, b):
    if a == 0: return 0
    if a % 2 == 0: return 2 * russian_rec(a / 2, b)
    return b + 2 * russian_rec((a - 1) / 2, b)