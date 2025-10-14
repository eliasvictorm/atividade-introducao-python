numeros = []                                            # Estrutura vazia

print("QUESTÃO 3 - Transforma valores negativos em zero")
for i in range(10):
    numeros.append(int(input("Digite um número inteiro: ")))

print("Números digitados:", numeros)


for i in range(len(numeros)):                           # Substitui valores negativos por 0
    if numeros[i] < 0:
        numeros[i] = 0

print("Números após a substituição dos negativos por zero:", numeros)
