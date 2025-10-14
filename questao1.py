#1.1 - Receba o nome e a nota de 10 alunos e guarde em
# uma estrutura de dados.

alunos = []

for i in range(10):
    nome = input(f"Digite o nome do aluno: ")
    nota = float(input(f"Informe a nota: "))
    alunos.append({"nome": nome, "nota": nota})

# 1.2 - Calcule a média das notas recebidas.

soma_notas = sum(aluno["nota"] for aluno in alunos)
media = soma_notas / len(alunos)

# 1.3 - Imprima a média das notas.

print(f"\nMédia das notas: {media:.2f}")

# 1.4 - Imprima a maior e a menor nota, bem como quais
# os alunos que obtiveram essas notas.

maior_nota = max(aluno["nota"] for aluno in alunos)
menor_nota = min(aluno["nota"] for aluno in alunos)

aluno_maior = [aluno["nome"]
               for aluno in alunos
               if aluno["nota"] == maior_nota]

aluno_menor = [aluno["nome"]
               for aluno in alunos
               if aluno["nota"] == menor_nota]

print(f"\nMaior nota: {maior_nota:.2f} - Aluno(s): {', '.join(aluno_maior)}")
print(f"\nMenor nota: {menor_nota:.2f} - Aluno(s): {', '.join(aluno_menor)}")


# 1.5 - Imprima uma listagem contendo o nome e nota dos
# alunos, que obtiveram notas abaixo da média.

print("\nAlunos abaixo da média:")
for aluno in alunos:
    if aluno["nota"] < media:
        print(f"{aluno['nome']} - Nota: {aluno['nota']:.2f}")


# 1.6 – Imprima uma listagem contendo os nomes e notas
# dos alunos, que obtiveram notas maiores ou iguais à média.

print("\nAlunos com notas iguais ou acima da média: ")
for aluno in alunos:
    if aluno["nota"] >= media:
        print(f"{aluno['nome']} - Nota: {aluno['nota']:.2f}")