dia = int(input("Qual o dia de hoje?"))
pedidoPizza = int(input('Quantas pizzas comprou?'))
pedidoBebida = int(input('Quantas bebidas comprou?'))
pedidoBolo = int(input('Quantos bolos comprou?'))
pedidoDoce = int(input('Quantos doces comprou?'))
# Declarando Variavéis
diaFesta = 26
pedidoMinimoPizza = 10
pedidoMinimoBebida = 12
pedidoMinimoBolo = 5
pedidoMinimoDoce = 600

if diaFesta == dia: 
    print('Ana esta fazendo as compras no dia da festa!')
else:
    print('Ana esta fazendo compra adiantada')

if(pedidoMinimoPizza >= pedidoPizza):
    print('Ana não comprou pizzas suficientes!')

if(pedidoMinimoBebida):
    print('Ana comprou mais bebidas que o necessário!')

if(pedidoMinimoBolo):
    print('Ana excedeu a compra de bolos!')

if(pedidoMinimoDoce):
    print('Ana não comprou doces suficientes!')

