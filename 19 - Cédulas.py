N = int(input())
cont = 0
print(f'{N}')
while(N >= 100):
    cont += 1
    N -= 100
print(f'{cont} nota(s) de R$ 100,00')
cont = 0
while(N >= 50):
    cont += 1
    N -= 50
print(f'{cont} nota(s) de R$ 50,00')
cont = 0
while(N >= 20):
    cont += 1
    N -= 20
print(f'{cont} nota(s) de R$ 20,00')
cont = 0
while(N >= 10):
    cont += 1
    N -= 10
print(f'{cont} nota(s) de R$ 10,00')
cont = 0
while(N >= 5):
    cont += 1
    N -= 5
print(f'{cont} nota(s) de R$ 5,00')
cont = 0
while(N >= 2):
    cont += 1
    N -= 2
print(f'{cont} nota(s) de R$ 2,00')
cont = 0
while(N >= 1):
    cont += 1
    N -= 1
print(f'{cont} nota(s) de R$ 1,00')
