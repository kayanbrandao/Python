A, B, C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
delta = (B * B) - (4 * A * C)
if delta >= 0 and A != 0:
    print(f'R1 = {((B*(-1) + (delta ** 0.5)) / (2 * A)):.5f}')
    print(f'R1 = {((B*(-1) - (delta ** 0.5)) / (2 * A)):.5f}')
else:
    print('Impossivel calcular')