lista_palavras = []
for i in range(10):
    lista_palavras.append(input(f"Informe uma palavra"))
arquivo = open("lista.txt", "w+")
arquivo.writelines(lista_palavras)