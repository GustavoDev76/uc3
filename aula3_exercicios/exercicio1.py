#Exercício 1: O Catálogo de Streaming

#Tema: Entretenimento

#Vamos criar o modelo de dados básico de uma plataforma como a Netflix.

##Tarefa:
##1. Crie uma classe chamada Filme.
#2. No método __init__, ela deve receber o titulo e a duracao (em minutos).
#3. Todo filme deve nascer com um atributo assistido definido como False.
#4. Crie um método chamado marcar_como_assistido(self) que simplesmente
#muda o atributo assistido para True e imprime: "O filme [nome_do_filme] foi
#assistido!"

#Teste: Crie dois filmes. Marque apenas o primeiro como assistido. Imprima o atributo
#assistido de ambos para confirmar se apenas um mudou.

class Filme:
    def __init__ (self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.assistindo = False

    def marcar_como_assistido(self):
        self.assistindo = True
        print("o filme [nome_do_filme] foi assistido")

filme1 = Filme("Psicopata Americano)", 102)
filme2 = Filme("Clube da Luta", 139)

filme1.marcar_como_assistido()

print(f"status do filme {filme1.titulo}: assistindo: {filme1.assistindo}")
print(f"Duracao do filme: {filme1.duracao} minutos")

print(f"status do filme {filme2.titulo}: assistindo: {filme2.assistindo}")
print(f"duracao do filme2: {filme2.duracao} minutos")