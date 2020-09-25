lista_letras = list(input("Escreva uma palavra"))
palavraResultado = ""
for letra in range(len(lista_letras)):
    if (letra % 2):
        lista_letras[letra] = ""
    else:
        palavraResultado = palavraResultado + lista_letras[letra]
print(palavraResultado)