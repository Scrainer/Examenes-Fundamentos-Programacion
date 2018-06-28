palabra = 'aabbbccdefggh'
final = ''
actual = ''
for letra in palabra:
    if letra != actual:
        final = final + letra
        actual = letra
print("Final:")
print(final)



for i in range(1, 10):
    print(str(i) * i)


for i in range(1, 10):
    for j in range(i):
        print(i, end='')
    print()