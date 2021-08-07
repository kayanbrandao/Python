A, B, C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
A_TRIANGLE = (A * C) / 2
A_CIRCLE = 3.14159 * (C ** 2)
A_TRAPEZE = ((A + B) * C) / 2
A_SQUARE = B * B
A_RECTANGLE = A * B
print(f'TRIANGULO: {A_TRIANGLE:.3f}\nCIRCULO: {A_CIRCLE:.3f}\nTRAPEZIO: {A_TRAPEZE:.3f}\nQUADRADO: {A_SQUARE:.3f}\nRETANGULO: {A_RECTANGLE:.3f}')