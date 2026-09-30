#Declaração de variáveis
numVoltas: float = 0
extensaoCircuito: float = 0
tempo: float = 0
velocidadeMedia: float = 0
distancia: float = 0

def calcularVelocidade(numVoltas, extensaoCircuito, tempo):
    distancia = numVoltas * extensaoCircuito
    distanciaKm = distancia / 1000
    tempoHora = tempo / 60
    velocidadeMedia = distanciaKm / tempoHora
    print("A velocidade média é: ", velocidadeMedia)

def main():
    numVoltas = float(input("Digite o número de voltas: "))
    extensaoCircuito = float(input("Digite a extensão do circuito em metros: "))
    tempo = float(input("Digite a duração do tempo em minutos: "))

    calcularVelocidade(numVoltas, extensaoCircuito, tempo)

if (__name__ == '__main__'):
        main()
