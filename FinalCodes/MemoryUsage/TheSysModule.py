import sys

a = 1
b = 3.123666
c = [a, b]
d = ['hello hello hello hello hello hello hello hello hello hello hello hello']
e = d[0]

for obj in [a, b, c, d, e]:
    print(obj, sys.getsizeof(obj))

print(a.__sizeof__())

