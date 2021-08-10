N = int(input())
cont = 0
while(N >= 365):
    cont += 1
    N -= 365
print(f'{cont} ano(s)')
cont = 0
while(N >= 30):
    cont += 1
    N -= 30
print(f'{cont} mes(es)')
print(f'{N} dia(s)')