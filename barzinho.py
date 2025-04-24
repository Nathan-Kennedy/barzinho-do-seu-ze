def barzinho_do_seu_ze():
    import os

"""Mostra um menu de bebidas com seus preços"""

    bebidas = {
        '1': {'nome': 'Skol 269ml', 'preco': 5.00},
        '2': {'nome': 'Heineken 369ml', 'preco': 9.00},
        '3': {'nome': 'Brahma 269ml', 'preco': 6.90}
    }

    carrinho = []

"""Dá boas-vindas ao cliente com uma saudação estilosa"""

    print("Fala meu patriarca! Bem-vindo ao *Barzinho do seu Zé* 🍻\n")

"""Usa o sistema de Loop While e 
Permite que o cliente escolha bebidas digitando o número correspondente"""

    while True:
        print("Escolha sua bebida:")
        for key, bebida in bebidas.items():
            print(f"{key} - {bebida['nome']} - R${bebida['preco']:.2f}")

        escolha = input("Digite o número da bebida desejada: ").strip()

        if escolha in bebidas:
            bebida_escolhida = bebidas[escolha]
            carrinho.append(bebida_escolhida)
            print(f"Você escolheu {bebida_escolhida['nome']} 🥂")
        else:
            print("Não entendi, pode repetir?")
            continue

        continuar = input("Deseja escolher mais alguma bebida? (sim/não): ").strip().lower()
        if continuar != 'sim':
            break
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela

"""Após cada escolha, pergunta se ele quer escolher mais alguma,
Caso não tenha redireciona para o caixa"""

    print("\n🧾 Indo pro caixa...\n")
    total = (item['preco'] for item in carrinho)
    print("Resumo da compra:")
    resumo = {}
    for item in carrinho:
        nome = item['nome']
        if nome in resumo:
            resumo[nome]['quantidade'] += 1
            resumo[nome]['subtotal'] += item['preco']
        else:
            resumo[nome] = {'quantidade': 1, 'subtotal': item['preco']}

    for nome, info in resumo.items():
        print(f"{nome} x{info['quantidade']} - R${info['subtotal']:.2f}")

"""Finaliza com uma mensagem de agradecimento"""

    print(f"\n💰 Total a pagar: R${total:.2f}")
    print("Valeu pela preferência, meu patriarca! Volte sempre 😎")

"""Atalho para usar o comando no terminal: python barzinho.py"""

if __name__ == "__main__":
    barzinho_do_seu_ze()
