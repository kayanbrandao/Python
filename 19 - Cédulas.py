valor = int(input())
n = [100, 50, 20, 10, 5, 2, 1]
print(f'{valor}')
for n in n:
    qt_notas = int(valor / n)
    print(f'{qt_notas} nota(s) de R$ {n},00')
    valor -= qt_notas * n