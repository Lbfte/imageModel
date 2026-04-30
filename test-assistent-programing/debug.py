#codigo debug versao corrigida

# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# A base de cálculo (subtotal) é definida antes da aplicação de taxas externas (impostos/descontos)
subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# Converte o valor percentual em um fator decimal para reduzir o valor bruto do subtotal
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# A ordem das operações garante que o imposto incida sobre o subtotal cheio, enquanto o desconto subtrai valor do cliente
total = subtotal + imposto - desconto

# EXIBIÇÃO
# Definição de constantes de estilo para manter a padronização visual e facilitar ajustes futuros na largura do recibo
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)

# O uso de :.2f garante que o valor monetário sempre exiba duas casas decimais, mesmo que o resultado seja redondo
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Validação lógica: a linha de desconto só é exibida se houver um benefício real, evitando poluição visual no recibo
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
# round(total, 2) previne erros de precisão de ponto flutuante em cálculos financeiros no Python
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)

#codigo antigo (com erros)

# # ENTRADA DE DADOS
# cliente = input("Qual é seu nome? ")

# qtd1 = int(input("Quantidade do item 1: "))
# item1 = float(input(Preço do item 1? ))

# qtd2 = int(input("Quantidade do item 2: "))
# item2 = float(input("Preço do item 2? "))

# qtd3 = int(input("Quantidade do item 3: "))
# item3 = float(input("Preço do item 3? "))

# # CÁLCULOS DOS ITENS
# total_item1 = qtd1 * item1
# total_item2 = qtd2 * item2
# total_item3 = qtd3 * item3

# subtotal = total_item1 + total_item2 + total_item3
# imposto = subtotal * 0.10

# # DESCONTO
# desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# desconto = subtotal * (desconto_cupom / 100)

# # TOTAL FINAL
# total = subtotal + imposto - desconto

# # EXIBIÇÃO
# linha = "=" * 31
# separador = "-" * 31

# print(linha)
# print(f" Cliente: {cliente}")
# print(linha)
# print(f" Item 1:        R$ {total_item1:.2f}")
# print(" Item 2:        R$ {total_item2:.2f}")
# print(f" Item 3:        R$ {total_item3:.2f}")
# print(separador)
# print(f" Subtotal:      R$ {subtotal:.2f}")
# print(f" Imposto (10%): R$ {imposto:.2f}")

# if desconto_cupom > 0: 
# print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

# print(linha)
# print(f" TOTAL:         R$ {round(total, 2):.2f}")
# print(linha)