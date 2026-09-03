#PARTE 3: Laços de Repetição e Processamento de Dados

#exercicio 5. Filtro de Usuários Ativos: Dado o seguinte "banco de dados" fictício:
#Python
#usuarios = [
#{"id": 1, "nome": "Ana", "email": "ana@email.com", "ativo": True},
#{"id": 2, "nome": "Beatriz", "email": "bea@email.com", "ativo": False},
#{"id": 3, "nome": "Carlos", "email": "car@email.com", "ativo": True}
#]

#Tarefa: Escreva um laço for que percorra esta lista e crie uma nova lista chamada
#emails_ativos contendo apenas os e-mails dos usuários onde "ativo" é True. No
#final, imprima a lista de e-mails.

usuarios = [
    {"id": 1, "nome": "ana", "email": "ana@email.com", "ativo": True},
    {"id": 2, "nome": "beatriz", "email": "bea@gmail.com", "ativo": False},
    {"id": 3, "nome": "carlos", "email": "car@gmail.com", "ativo": True}
]

emails_ativos = []

for i in usuarios:
    if i ["ativo"]:
        emails_ativos.append(i["email"])

print("E-mails Ativos:")
for i in emails_ativos:
    print(i)

#exercicio 6. Limpeza de Dados de Frete: Um sistema enviou uma lista de fretes, mas alguns valores
    
#estão negativos por erro de processamento:
    
#Python
#fretes = [15.50, -2.00, 10.00, 25.00, -5.50, 30.00]
#Tarefa: Crie um script que percorra a lista e exiba apenas os valores positivos.

fretes = [15.50, -2.00, 10.00, 25.00, -5.50, 30.00]

for i in fretes:
    if i >= 0:
        print(i)

#exercicio 7. Contagem de Estoque Crítico: Dada a lista de quantidades em stock: itens_estoque
#= [12, 3, 8, 2, 15, 4, 20]. Tarefa: Escreva um código que conte quantos produtos
#têm menos de 5 unidades e exiba o total.

itens_estoque = [12, 3, 8, 2, 15, 4, 20]

estoque_critico = 0

print("Estoques Criticos:")
for i in itens_estoque:
    if i < 5:
        estoque_critico = estoque_critico + 1
print(f"Existem {estoque_critico} Itens No Estoque Critico")