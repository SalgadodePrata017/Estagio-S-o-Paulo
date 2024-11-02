day1 = 1#int(input("Informe o valor do faturamento do dia 1 do mês: "))
day2 = 250#int(input("Informe o valor do faturamento do dia 2 do mês: "))
day3 = 145#int(input("Informe o valor do faturamento do dia 3 do mês: "))
day4 = 253#int(input("Informe o valor do faturamento do dia 4 do mês: "))
day5 = 356#int(input("Informe o valor do faturamento do dia 5 do mês: "))
day6 = 847#int(input("Informe o valor do faturamento do dia 6 do mês: "))
day7 = 61#int(input("Informe o valor do faturamento do dia 7 do mês: "))
day8 = 6841#int(input("Informe o valor do faturamento do dia 8 do mês: "))
day9 = 15#int(input("Informe o valor do faturamento do dia 9 do mês: "))
day10 = 165#int(input("Informe o valor do faturamento do dia 10 do mês: "))
day11 = 156#int(input("Informe o valor do faturamento do dia 11 do mês: "))
day12 = 165#int(input("Informe o valor do faturamento do dia 12 do mês: "))
day13 = 354#int(input("Informe o valor do faturamento do dia 13 do mês: "))
day14 = 5410#int(input("Informe o valor do faturamento do dia 14 do mês: "))
day15 = 6510#int(input("Informe o valor do faturamento do dia 15 do mês: "))
day16 = 518#int(input("Informe o valor do faturamento do dia 16 do mês: "))
day17 = 841#int(input("Informe o valor do faturamento do dia 17 do mês: "))
day18 = 61#int(input("Informe o valor do faturamento do dia 18 do mês: "))
day19 = 61#int(input("Informe o valor do faturamento do dia 19 do mês: "))
day20 = 215#int(input("Informe o valor do faturamento do dia 20 do mês: "))
day21 = 848#int(input("Informe o valor do faturamento do dia 21 do mês: "))
day22 = 15#int(input("Informe o valor do faturamento do dia 22 do mês: "))
day23 = 651#int(input("Informe o valor do faturamento do dia 23 do mês: "))
day24 = 7841#int(input("Informe o valor do faturamento do dia 24 do mês: "))
day25 = 174#int(input("Informe o valor do faturamento do dia 25 do mês: "))
day26 = 17#int(input("Informe o valor do faturamento do dia 26 do mês: "))
day27 = 871#int(input("Informe o valor do faturamento do dia 27 do mês: "))
day28 = 871#int(input("Informe o valor do faturamento do dia 28 do mês: "))
day29 = 841#int(input("Informe o valor do faturamento do dia 29 do mês: "))
day30 = 874#int(input("Informe o valor do faturamento do dia 30 do mês: "))
day31 = 2534#int(input("Informe o valor do faturamento do dia 31 do mês: "))

mes = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15, day16, day17,day18, day19, day20, day21, day22, day23, day24, day25, day26, day27, day28, day29, day30, day31]

meta_mes = {
    'Dia 1': day1,
    'Dia 2': day2,
    'Dia 3': day3,
    'Dia 4': day4,
    'Dia 5': day5,
    'Dia 6': day6,
    'Dia 7': day7,
    'Dia 8': day8,
    'Dia 9': day9,
    'Dia 10': day10,
    'Dia 11': day11,
    'Dia 12': day12,
    'Dia 13': day13,
    'Dia 14': day14,
    'Dia 15': day15,
    'Dia 16': day16,
    'Dia 17': day17,
    'Dia 18': day18,
    'Dia 19': day19,
    'Dia 20': day20,
    'Dia 21': day21,
    'Dia 22': day22,
    'Dia 23': day23,
    'Dia 24': day24,
    'Dia 25': day25,
    'Dia 26': day26,
    'Dia 27': day27,
    'Dia 28': day28,
    'Dia 29': day29,
    'Dia 30': day30,
    'Dia 31': day31,
}

minimo_mes = min(mes)
dia_minimo_mes = min(meta_mes)

maximo_mes = max(mes)
dia_maximo_mes = max(meta_mes)

print(f'O valor do menor faturamento no mês foi: R$ {minimo_mes} no {dia_minimo_mes}')
print(f'O valor do maior faturamento no mês foi: R$ {maximo_mes} no {dia_maximo_mes}')

faturamento_diario = 1231.48
contador = 0
print()
print("Dias no qual o faturamento diario atingiu a média mensal:")

for nome, valor in meta_mes.items():
    if valor >= faturamento_diario:
        print(f'{nome}: R$ {valor}')
        contador += 1
print()
print(f'Total de variáveis exibidas: {contador}')
        