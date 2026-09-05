''' Exercício 3: O App do Banco
Tema: FinTech (Regras de Negócio e Validação)
No backend de um banco, um objeto não pode fazer o que quiser. Precisamos de regras de
negócio (condicionais if/else) dentro dos métodos.
Tarefa:
1. Crie uma classe ContaBancaria que receba no __init__ o nome do titular.
2. O saldo deve começar sempre em 0.0.
3. Crie um método depositar(self, valor). Ele deve somar o valor ao saldo e
imprimir o novo saldo.
4. Crie um método sacar(self, valor). Regra de ouro: O objeto só pode sacar
se o valor for menor ou igual ao saldo.
○ Se houver dinheiro, subtraia do saldo e imprima o valor sacado.
○ Se não houver, imprima "Saque negado: Saldo insuficiente."
Teste: Crie uma conta para você. Deposite R$ 100,00. Tente sacar R$ 150,00 (deve ser
negado). Tente sacar R$ 50,00 (deve ser aprovado). '''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saldo Sacado")
        else:
            print("Saldo Insuficiente")

conta = ContaBancaria("Gustavo", 66.00)

conta.depositar(100.00)

conta.sacar(67.00)