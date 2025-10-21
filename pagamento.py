def pagamento_type():

    from enum import Enum
    from functools import reduce


    class PagamentoType(Enum):
        BOLETO = "Boleto"
        CARTAO_CREDITO = "Cartão de Crédito"
        PIX = "Pix"
        DEBITO_BANCARIO = "Débito Bancário"


    class Pagamento:
        tipo_pagamento: PagamentoType
        valor: float


    lista_pagamentos = []


    def adicionar_pagamento(tipo: PagamentoType, valor: float):
        pagamento = Pagamento()
        pagamento.tipo_pagamento = tipo
        pagamento.valor = valor
        lista_pagamentos.append(pagamento)


    valor_total = 1000.0

    while [
        reduce(lambda acumulator, curr: acumulator + curr.valor, lista_pagamentos, 0)
        < valor_total
    ]:
        print(f"Valor total a ser pago: {valor_total}")
        print(f"Valor já pago: {sum(p.valor for p in lista_pagamentos)}")
        print("Escolha o tipo de pagamento:")
        for i, tipo in enumerate(PagamentoType):
            print(f"{i + 1}. {tipo.value}")

        escolha = int(input("Digite o número correspondente ao tipo de pagamento: ")) - 1
        tipo_selecionado = list(PagamentoType)[escolha]

        valor_pago = float(input("Digite o valor a ser pago: "))

        if sum(p.valor for p in lista_pagamentos) + valor_pago > valor_total:
            print("O valor pago excede o valor total. Tente novamente.")
        else:
            adicionar_pagamento(tipo_selecionado, valor_pago)
            print("Pagamento adicionado com sucesso.\n")