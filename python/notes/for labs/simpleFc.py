def smallest(x, y, z):
    if x < y:
        if x < z:
            return x
    if y < x:
        if y < z:
            return y
    if z < x:
        if z < y:
            return z


def average(x, y, z):
    avg = (x + y + z) / 3
    return avg


print(smallest(10, 20, 30))
print(smallest(17, 5, 11))
print(smallest(23, 27, 4))
