vocales=['a', 'e', 'i', 'o', 'u']
consonantes=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
frase=input("Ingrese una frase: ")
frase=frase.replace("."," ")
l_frase=frase.split(" ")
total=0
for palabra in l_frase:
    if palabra.isalpha():
        vocal=0
        conson=0
        for letra in palabra:
            if letra in vocales:
                vocal=vocal+1
            else:
                conson=conson+1
        if vocal==conson:
            total=total+1

print("Cantidad de palabras que cumplen la condición: %d"%total)