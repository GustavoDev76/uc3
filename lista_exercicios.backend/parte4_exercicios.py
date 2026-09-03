#PARTE 4: Integração e Funções

#8. Calculadora de Património: Utilizando a lista de produtos que criou no Exercício 3,
#percorra o stock e calcule o Valor Total do Património (soma de quantidade * preco
#de todos os itens). Exiba o resultado com uma mensagem explicativa.

estoque = [
    {"id": 1, "nome": "sapato", "quantidade": 5, "preco": 100.00},
    {"id": 2, "nome": "bola", "quantidade": 10, "preco": 50.00},
    {"id": 3, "nome": "chinelo", "quantidade": 5, "preco": 35.00}
]

patrimonio = 0

for i in estoque:
    patrimonio += i["quantidade"] * i["preco"]

print(f"O preco de patrimonio total da empresa é de R${patrimonio}")


#9. Busca de Usuário por ID:
#Python
#base_usuarios = [
#{"id": 101, "nome": "Alice"},
#{"id": 102, "nome": "Bruno"},
#{"id": 103, "nome": "Carla"}
#]

#Tarefa: Peça ao utilizador para digitar um ID. Percorra a lista e, se encontrar o ID, imprima o
#nome do usuário. Se o laço terminar e não encontrar, imprima "Usuário não encontrado".

base_usuarios = [
{"id": 101, "nome": "Alice"},
{"id": 102, "nome": "Bruno"},
{"id": 103, "nome": "Carla"}
]

def encontrar_id(id):
    encontrado = False
    for i in base_usuarios:
        if id == i["id"]:
            encontrado = True
        return f"Usuario encontrado {i["nome"]}"

    if not encontrado:
        return "Usuario nao encontrado"

# Chamada / CallBack
print(encontrar_id(int(input("Digite o id do usuario para encontrar o usuario: "))))

#10. Modularização (Funções): Para evitar repetição de código (Princípio DRY), crie uma

#função chamada gerar_boas_vindas(nome).

#● A função deve retornar a frase: "Olá, [nome], bem-vindo ao servidor
#Python!".
#● Teste a função chamando-a e imprimindo o resultado.

def gerar_boas_vindas(nome):
    print(f"ola, {nome}, bem-vindo ao servidor python")

gerar_boas_vindas(input("digite seu nome:\n->"))