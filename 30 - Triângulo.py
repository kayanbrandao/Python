a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f'Perimetro = {(a + b + c):.1f}')
else:
    print(f'Area = {((a + b) / 2) * c:.1f}')