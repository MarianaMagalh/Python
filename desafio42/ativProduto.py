print("Cadastro de Produtos")

codigo = int(input("Qual o codigo do produto: "))
nome_produto = input("Qual o nome do produto: ")
estoque = input("Qual é o seu estoque: ")
preço = float(input("Qual o valor do produto: "))

print(f"\n\nCadastro feito com sucesso!\n Codigo: {codigo}\n Nomedo Produto: {nome_produto}\n Estoque: {estoque}\n Preço: R${preço}")