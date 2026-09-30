#Declaração de variáveis
precoProduto: float = 0
novoPreco: float = 0
vendaMensal: int = 0

def precoAtualizado(precoProduto, vendaMensal):
    if (vendaMensal < 500) and (precoProduto < 30):
        novoPreco = precoProduto * 1.1
        print("O novo preço é: ", novoPreco)
    elif(vendaMensal >= 500 and vendaMensal <1000) and (precoProduto >= 30 and precoProduto <80):
        novoPreco = precoProduto * 1.15
        print("O novo preço é: ", novoPreco)
    elif(vendaMensal >= 1000) and (precoProduto >= 80):
        novoPreco = precoProduto * 0.95
        print("O novo preço é: ", novoPreco)
    else:
        novoPreco = precoProduto
        print("O preço é: ", novoPreco)

    

def main():
    precoProduto = float(input("Digite o valor do produto: "))
    vendaMensal = int(input("Digite a quantidade de venda mensal: "))
    precoAtualizado(precoProduto,vendaMensal)
if (__name__ == '__main__'):
    main()