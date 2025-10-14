numeros = []                                        # Estrutura vazia

print("QUESTÃO 2 - Verifica se número faz parte da estrutura montada pelo usuário  ")
for i in range(10):
    numeros.append(int(input("Digite 10 números inteiros:")))

print('n° digitados:',numeros)                      # lista os 10 números

n = (int(input("Digite outro número: ")))

if n not in numeros:                                # Verifica se número está na estrutura
    print(f'O número {n} não se encontra na estrutura acima')
elif n in numeros:
    print(f'Número {n} se encontra na posição {numeros.index(n) + 1} da estrutura')
