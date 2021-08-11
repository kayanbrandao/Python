n1, n2, n3, n4 = input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
if media >= 7:
    print(f'Media: {media:.1f}\nAluno aprovado.')
elif media < 5:
    print(f'Media: {media:.1f}\nAluno reprovado.')
elif media >= 5 and media <= 6.9:
    ne = float(input())
    mediaFinal = (media + ne) / 2
    if mediaFinal >= 5:
        print(f'Media: {media:.1f}\nAluno em exame.\nNota do exame: {ne:.1f}\nAluno aprovado.\nMedia final: {mediaFinal:.1f}')
    elif mediaFinal < 5:
        print(f'Media: {media:.1f}\nAluno em exame.\nNota do exame: {ne:.1f}\nAluno reprovado.\nMedia final: {mediaFinal:.1f}')