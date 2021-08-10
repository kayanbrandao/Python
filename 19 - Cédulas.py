valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(f'{valor}')
for nota in notas:
    qt_notas = int(valor / nota)
    print(f'{qt_notas} nota(s) de R$ {nota},00')
    valor -= qt_notas * nota