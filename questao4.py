#4.1 - Solicite ao usuário que informe inicialmente os 6
#números sorteados na Mega Sena.

sorteados = []
print("Digite os 6 números sorteados da Mega Sena:")
for i in range(6):
    num = int(input(f"Número {i+1}: "))
    sorteados.append(num)

#4.2 - Em seguida, peça que ele digite os 6 números do cartão que jogou.

jogo = []
print("\nDigite os 6 números do seu jogo:")
for i in range(6):
    num = int(input(f"Número {i+1}: "))
    jogo.append(num)

#4.3 - Imprima a quantidade de pontos que ele fez no
#concurso.

acertos = set(sorteados) & set(jogo)

print("\nNúmeros sorteados:", sorteados)
print("Seus números:", jogo)
print(f"Você acertou {len(acertos)} número(s): {sorted(acertos)}")