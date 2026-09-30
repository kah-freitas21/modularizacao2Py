#Declaração de variáveis
tipo: int = 0
valor: float = 0
valorCorrigido: float = 0

def poupanca(tipo, valor):
    if (tipo == 1):
        valorCorrigido = valor * 1.03
        print ("O valor corrigido: ", valorCorrigido)
    elif (tipo == 2):
        valorCorrigido = valor * 1.05
        print("O valor corrigido: ", valorCorrigido)
  



def main():
    tipo = int(input("Digite o tipo de investimento 1- Poupança e 2- Renda Fixa: "))
    valor = float(input("Digite o valor do investimento: "))
    poupanca(tipo, valor)

if (__name__ == '__main__'):
        main()