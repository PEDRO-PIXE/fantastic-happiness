def  contratar_plano_streaming(banco_dados,id_plano,id_pedido,meses_fidelidade):

    ##assinar plano##
    planos = banco_dados.get("plano_streaming",{})

    if id_plano not in planos:
        return False

    if meses_fidelidade <1:
        return False 

    pedido = pedidos[id_plano] 

    if id_plano not in pedidos:
        return False

    pedido = pedido[id_pedido]
    plano = plano[id_plano]

    nome_do_plano = plano["apex"]
    mensalidade = plano["mensalidade"]

    subtotal =mensalidade * meses_fidelidade

    if meses_fidelidade >= 12:
        subtotal=subtotal*0.85
        subtotal = round(subtotal,2)

        item = {
            "categoria":"streaming"
            "descrição": nome_do_plano,
            "qtd": meses_fidelidade,
            "subtotal": subtotal
    }

    if"carrinho" not in pedido:
        pedido["carrinho"] =[]

        pedido["carrinho"].append(item)

        pedido["valor_bruto"] = round(pedido.get("valor_bruto",0)+subtotal,2)
        pedido["valor_liquido"] = pedido["valor_bruto"]

        return True
    