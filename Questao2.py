import re
senha = input("Informe uma senha")
if re.search("[_@$]", senha) and re.search("[0-9]", senha):
    print("Senha válida")
else:
    print("Senha inválida")