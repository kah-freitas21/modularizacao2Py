# Declaração de variáveis
n: int = 0
fatorial: int = 1
serie: float = 1
resultado: float = 0


def fatorialNum(valor):
    fatorial = 1
    for i in range(1, valor + 1, 1):
        fatorial = fatorial * i
    return fatorial

def divisao(primeiro, segundo):
    resultado = primeiro / segundo
    return resultado

def main():
    n = int(input("Digite o valor de N: "))
    serie = 1

    for i in range(1, n + 1, 1):
        fatorial = fatorialNum(i)
        resultado = divisao(1, fatorial)
        serie = serie + resultado
    print("O resultado da série é: ", serie)


if (__name__ == '__main__'):
    main()