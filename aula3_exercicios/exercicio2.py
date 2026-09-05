#Exercício 2: A Casa Inteligente

#Tema: Internet das Coisas (IoT)

#Você está programando o backend de um aplicativo de Smart Home (Casa Inteligente).

#Tarefa:
#1. Crie uma classe chamada ArCondicionado
#2. No __init__, a classe não precisa receber nenhum parâmetro externo, mas deve
#definir dois atributos padrão: ligado (começa como False) e temperatura
#(começa em 24).
#3. Crie um método ligar(self) que muda o status para True.
#4. Crie um método desligar(self) que muda o status para False.
#5. Crie um método aumentar_temperatura(self) que aumenta a temperatura em
#1 grau.
#6. Crie um método diminuir_temperatura(self) que diminui a temperatura em 1
#grau.

#Teste: Instancie um ar-condicionado. Ligue-o. Aumente a temperatura duas vezes e
#diminua uma vez. Imprima o status e a temperatura final para verificar se está em 25 graus.

class ArCondicionado:
    def __init__(self):
        self.ligado = False
        self.temperatura = 24

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def aumentar_temperatura(self):
        self.temperatura += 1

    def diminuir_temperatura(self):
        self.temperatura -= 1

ar_condicionado = ArCondicionado()

ar_condicionado.ligar()
ar_condicionado.desligar()

ar_condicionado.aumentar_temperatura()
ar_condicionado.diminuir_temperatura()

print(f"Ligado: {ar_condicionado.ligado}")
print(f"Temperatura: {ar_condicionado.temperatura}")


