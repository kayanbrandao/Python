a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
if a < b and b < c:
    print(f'{a}\n{b}\n{c}\n')
    print(f'{a}\n{b}\n{c}')
if a < c and c < b:
    print(f'{a}\n{c}\n{b}\n')
    print(f'{a}\n{b}\n{c}')
if b < a and a < c:
    print(f'{b}\n{a}\n{c}\n')
    print(f'{a}\n{b}\n{c}')
if b < c and c < a:
    print(f'{b}\n{c}\n{a}\n')
    print(f'{a}\n{b}\n{c}')
if c < a and a < b:
    print(f'{c}\n{a}\n{b}\n')
    print(f'{a}\n{b}\n{c}')
if c < b and b < a:
    print(f'{c}\n{b}\n{a}\n')
    print(f'{a}\n{b}\n{c}')
