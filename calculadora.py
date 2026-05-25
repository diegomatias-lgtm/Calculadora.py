
def subtracao(n1, n2):
    res = n1 - n2
    print("Resultado da subtracao:", res)
    return res

def multiplicacao(n1, n2):
    res = n1 * n2
    print("Resultado da multiplicacao:", res)
    return res

def divisao(n1, n2):
    # Nota: Radon analisará a complexidade aqui se houver verificações
    res = n1 / n2
    print("Resultado da divisao:", res)
    return res

def soma(n1, n2):
    res = n1 + n2
    print("Resultado da soma:", res)
    return res

def potencia(a, b):
    return a ** b

def minha_calculadora():
    print("Minha Calculadora")
    opcao = 0

    while opcao != 5:
        print("\nescolha a opcao:")
        print("1: subtracao")
        print("2: Multiplicacao")
        print("3: Divisao")
        print("4: soma")
        print("5: Sair")

        try:
            opcao = int(input("Escolha:"))
        except ValueError:
            print("Por favor, digite um número.")
            continue

        if 1 <= opcao <= 4:
            n1 = int(input("Informe Primeiro numero:"))
            n2 = int(input("Informe Segundo numero:"))

            if opcao == 1:
                subtracao(n1, n2)
            elif opcao == 2:
              multiplicacao(n1, n2)
            elif opcao == 3:
                divisao(n1, n2)
            elif opcao == 4:
                soma(n1, n2)
        
        elif opcao == 5:
            print("encerrado")

if __name__ == "__main__":
    minha_calculadora()