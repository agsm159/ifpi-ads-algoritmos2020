#02.Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
# O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional.
# Qual é o custo total de atacado para 60 cópias?

#Entrada

preço_do_livro = 24.95
livro_com_desconto = preço_do_livro * 40 / 100

#Processamento

preço_da_compra_livros = livro_com_desconto * 60
preço_transporte = 3 + 0.75 * 59
total = preço_da_compra_livros + preço_transporte

#Saída

print('O custo total de atacado para 60 cópias é {:.2f}'.format(total))
