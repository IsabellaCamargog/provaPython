from Pessoa import Pessoa
from Emprestimo import Emprestimo

pessoa = Pessoa("Isabella")
emprestimo = Emprestimo("Monitor", "31/12/2021")
pessoa.listaEmprestimos.append(emprestimo)
emprestimo = Emprestimo("Cabo HDMI", "31/12/2021")
pessoa.listaEmprestimos.append(emprestimo)
for emprestimo in pessoa.listaEmprestimos:
    print(f"Equipamento: {emprestimo.nome_equipamento} Data de devolução: {emprestimo.data_devolucao} ")