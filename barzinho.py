import os

def barzinho_do_seu_ze():
    """Simula um sistema de pedidos em um bar fictício."""

    bebidas = {
        '1': {'nome': 'Skol 269ml', 'preco': 5.00},
        '2': {'nome': 'Heineken 369ml', 'preco': 9.00},
        '3': {'nome': 'Brahma 269ml', 'preco': 6.90}
    }

    carrinho = []

    print("Fala meu patriarca! Bem-vindo ao *Barzinho do seu Zé* 🍻\n")

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

    print("\n🧾 Indo pro caixa...\n")

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

    total = sum(item['preco'] for item in carrinho)
    print(f"\n💰 Total a pagar: R${total:.2f}")
    print("Valeu pela preferência, meu patriarca! Volte sempre 😎")

    # Pausa ao final para o .exe não fechar de imediato
    input("\nPressione Enter para fechar o barzinho... 🍻")

if __name__ == "__main__":
    barzinho_do_seu_ze()
