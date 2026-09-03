class Cachorro:
    # METODO CONSTRUCTOR:
    def __init__(self, nome, raca, tamanho, cor_pelo): # ATRIBUTOS DA CLASSE
        self.nome = nome
        self.raca = raca
        self.tamanho = tamanho
        self.cor_pelo = cor_pelo
        self.patas = 4



zeca = Cachorro("Zeca", "Viralata", "Médio", "Caramelo")
brutus = Cachorro("Brutus", "Pitbull", "Grande", "Preto")
mel = Cachorro("Mel", "Yorkshire", "Pequeno", "Marrom")

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ativo = True

    # MÉTODO DE UMA CLASSE
    def destaivar_conta(self):
        self.ativo = False

    def mudar_nome(self):
        self.nome = input("digite seu novo nome de usuario")

nova_conta = Usuario("Gustavo", "gustavo@gmail.com")

nova_conta.destaivar_conta()

print(nova_conta.ativo)


