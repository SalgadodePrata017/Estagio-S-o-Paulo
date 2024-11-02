vlr1 = 67836.43 #input("Digite o valor de faturamento de SP: ")
vlr2 = 36678.66 #input("Digite o valor de faturamento do RJ: ")
vlr3 = 29229.88 #input("Digite o valor de faturamento de MG: ")
vlr4 = 27165.48 #input("Digite o valor de faturamento do EP: ")
vlr5 = 19849.53 #input("Digite o valor de faturamento dos Outros: ")
result = vlr1 + vlr2 + vlr3 + vlr4 + vlr5
pct1 = (vlr1 / result) * 100
pct2 = (vlr2 / result) * 100
pct3 = (vlr3 / result) * 100
pct4 = (vlr4 / result) * 100
pct5 = (vlr5 / result) * 100

print()
print(f'O percentual de faturamento do estado de São Paulo/SP em relação ao valor total mensal da distribuidora foi de: {pct1:,.2f}%')
print()
print(f'O percentual de faturamento do estado do Rio de Janeiro/RJ em relação ao valor total mensal da distribuidora foi de: {pct2:,.2f}%')
print()
print(f'O percentual de faturamento do estado de Minas Gerais/MG em relação ao valor total mensal da distribuidora foi de: {pct3:,.2f}%')
print()
print(f'O percentual de faturamento do estado do Espirito Santo/EP em relação ao valor total mensal da distribuidora foi de: {pct4:,.2f}%')
print()
print(f'O percentual de faturamento dos Outros estados em relação ao valor total mensal da distribuidora foi de: {pct5:,.2f}%')
print()