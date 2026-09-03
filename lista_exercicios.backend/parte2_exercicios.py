#PARTE 2: Estruturas de Dados (JSON/Dicionários)

#exercicio 3. Modelagem de Produto: No back-end, os dados trafegam como JSON (Dicionários em

#Python). Crie uma lista chamada estoque contendo 3 dicionários. Cada dicionário deve
#representar um produto com as chaves: id, nome, quantidade e preco.
#● Após criar a lista, adicione um novo produto usando o método .append().
#● Imprima no terminal apenas o nome do segundo produto da lista.

estoque = [
    {"id": 1, "nome": "sapato", "quantidade": 5, "preco": 100.00},
    {"id": 2, "nome": "bola", "quantidade": 10, "preco": 50.00},
    {"id": 3, "nome": "chinelo", "quantidade": 5, "preco": 35.00}
]

estoque.append({"id": len(estoque)+1, "nome": "bicicleta", "quantidade": 20, "preco": 800.00},)

print(estoque[1]["nome"])

#print(len(estoque))


#exercicio 4. Atualização de Status: Imagine que recebeu um objeto de um serviço de entrega:
#Python 
#pedido = {
#"cliente": "João Silva",
#"prato": "Hambúrguer Artesanal",
#"status": "em preparo"
#}

# Tarefa: Altere o valor da chave "status" para "saiu para entrega" e imprima o
#dicionário completo para confirmar a alteração.


pedido = {
    "cliente": "joao silva",
    "prato": "hamburguer aresanal",
    "status": "em preparo"
}

pedido["status"] = "saiu para entrega"

print(pedido)