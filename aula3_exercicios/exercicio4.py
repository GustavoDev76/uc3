'''Exercício 4: O Sistema de Transferência

Tema: FinTech (Interação entre Objetos)

Chegou a hora de fazer um objeto interagir diretamente com outro objeto! Vamos simular
uma transferência via PIX entre duas contas diferentes.

Tarefa:
1. Crie uma classe chamada CarteiraDigital.
2. O método __init__ deve receber o nome_titular e o saldo_inicial.
3. Crie um método chamado transferir_pix(self, valor,
carteira_destino). O parâmetro carteira_destino será outro objeto da
mesma classe CarteiraDigital.
4. Regra de negócio dentro do método:
○ Verifique se o objeto atual (self) tem saldo suficiente para a transferência
(self.saldo >= valor).
○ Se tiver dinheiro: Subtraia o valor do saldo atual (self) e some esse
mesmo valor ao saldo da carteira_destino. Imprima uma mensagem de
sucesso ("Transferência de R$ X realizada com sucesso!").
○ Se não tiver dinheiro: Imprima "Erro: Saldo insuficiente para realizar o PIX."

Teste: * Crie a carteira do cliente_a com R$ 500.00 de saldo.
● Crie a carteira do cliente_b com R$ 100.00 de saldo.
● Faça o cliente_a transferir R$ 150.00 para o cliente_b. (Exemplo de uso:
cliente_a.transferir_pix(150.00, cliente_b))
● Imprima o saldo final das duas carteiras para confirmar se o cliente_a ficou com
R$ 350.00 e o cliente_b com R$ 250.00.'''

class CarteiraDigital:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def transferir_pix(self, valor, carteira_destino):
        self.carteira_destino = CarteiraDigital
        if self.saldo >= valor:
            self.saldo -= valor
            carteira_destino.saldo =+ valor
            print(f"Tranfesrencia de R$ {valor:.2f} Realizado Com Sucesso")
        else:
            print("Error: Saldo Insuficiente para realizar o PIX")

cliente_1 = CarteiraDigital("Gustavo", 500.00)

cliente_2 = CarteiraDigital("Joana", 100.00)

cliente_1.transferir_pix(200.00, cliente_2)

print(f"Saldo Final  do {cliente_1.titular}: R${cliente_1.saldo}")
print(f"Saldo Final do {cliente_2.titular}: R${cliente_2.saldo}")