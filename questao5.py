def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    resultado = 0
    positivo = b>=0
    b = abs(b)
    for _ in range(b):
        resultado = soma(resultado, a)
    if not positivo:
        resultado = -resultado
    return resultado

def potencia(a, b):
    if b < 0:
        print("O expoente deve ser um número inteiro não negativo.")
        return None
    elif b == 0:
        return 1
    else:
        resultado = 1
        for _ in range(b):
            resultado = multiplicacao(resultado, a)
        return resultado
    
def pedir_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            
def main():
    print("---------- CALCULADORA ----------")
    num1 = pedir_inteiro("Digite o primeiro número inteiro: ")
    num2 = pedir_inteiro("Digite o segundo número inteiro: ")

    print("\n Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Potenciação")

    operacao = pedir_inteiro("Digite o número da operação desejada (1-4): ")

    if operacao == 1:
        resultado = soma(num1, num2)
        print(f"\nResultado da soma: {resultado}")
    elif operacao == 2:
        resultado = subtracao(num1, num2)
        print(f"\nResultado da subtração: {resultado}")
    elif operacao == 3: 
        resultado = multiplicacao(num1, num2)
        print(f"\nResultado da multiplicação: {resultado}")
    elif operacao == 4:
        resultado = potencia(num1, num2)
        if resultado is not None:
            print(f"\nResultado da potenciação: {resultado}")
    else:
        print("\nOperação inválida. Por favor, escolha uma operação entre 1 e 4.")

if __name__ == "__main__":
    main()