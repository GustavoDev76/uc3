#PARTE 1: Condicionais e Regras de Negócio

#1. Validador de Checkout: Crie um programa que simule a finalização de uma compra num:

#-commerce. O sistema deve receber:
#● valor_total (float)
#● cupom_valido (booleano - True/False)
#Regras:
#● Se o cupom for válido, aplique 10% de desconto no valor_total.
#● Se o saldo_usuario for maior ou igual ao valor final, exiba: "201 Created -
#Pedido realizado com sucesso".
#● Caso contrário, exiba: "402 Payment Required - Saldo insuficiente".
#2. Verificador de Acesso (Login): Crie uma lógica simples de autenticação. Defina duas
#variáveis fixas: username_cadastrado = "admin" e senha_cadastrada = "1234".
#Em seguida, use o input() para receber um nome de usuário e uma senha do teclado.
#● Se ambos forem iguais aos cadastrados, exiba: "Acesso concedido".
#● Caso contrário, exiba: "Credenciais inválidas".

valor_total = 10.0
saldo_usuario = 9.0
pergunta = input("voce tem cupom? s/n\n ").strip() .lower()

if pergunta == "sim":
    cupom_valido = True
else:
    cupom_valido = False

if cupom_valido:
    valor_total = valor_total * 0.9

if saldo_usuario >= valor_total:
    print("201 - Created - Pedido Realizado com Sucesso")
else:
    print("402 Payment Required - Saldo Insuficiente")


#2. Verificador de Acesso (Login): Crie uma lógica simples de autenticação. Defina duas
#variáveis fixas: username_cadastrado = "admin" e senha_cadastrada = "1234".
#Em seguida, use o input() para receber um nome de usuário e uma senha do teclado.
#● Se ambos forem iguais aos cadastrados, exiba: "Acesso concedido".
#● Caso contrário, exiba: "Credenciais inválidas".
#username_cadastrado = str(input("digite seu login: "))
#senha_cadastrada= str(input("digite sua senha: "))
username_cadastrado = "admin"
senha_cadastrada = "1234"  

if input("digite seu login: ") == username_cadastrado and input("digte sua senha de usuario: ") == senha_cadastrada:
    print("Acesso concedido")
else:
    print("Credenciais inválidas")