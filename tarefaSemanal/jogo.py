import random

opcoes = ["pedra", "papel", "tesoura"]

print("JOKENPÔ")

def escolhaUsuario():
    escolha = input("\nEscolha pedra, papel ou tesoura:\n").lower()
    while escolha not in ["pedra", "papel", "tesoura"]:
        escolha = input("Escolha invalida. Escolha pedra, papel ou tesoura: \n").lower()
    return escolha


def escolhaComputador():
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)


def vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif(jogador == "papel" and computador == "pedra") or \
        (jogador == "pedra" and computador == "tesoura") or \
        (jogador == "tesoura" and computador == "papel"):
        return "jogador"
    else:
        return "computador"
    
def jogando():
    while True:
        jogador = escolhaUsuario()
        computador = escolhaComputador()

        print(f"Você escolheu {jogador}")
        print(f"O computador escolheu {computador}")

        resultado = vencedor(jogador, computador)

        if resultado == "empate":
            print("Empate!")
        elif resultado == "jogador":
            print("\nVocê venceu!")
        elif resultado == "computador":
            print("\nO computador ganhou!")

        jogarNovamente = input("\nDejesa jogar novamente? (s/n)\n").lower()
        if jogarNovamente != 's':
            break

jogando()
