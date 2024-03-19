import random
def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias = 0
    print("bem vindo ao jogo jokenpô")
    print("escolha: pedra, papel, tesoura")

    while True:
        escolha_jogador = input("sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print("escolha invalida, tente novamente")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"computador escolheu: {escolha_computador}")

        resultado = define_vencedor(escolha_jogador, escolha_computador)
        print(resultado)

        if resultado == "voce ganhou":
            vitorias += 1
        elif resultado == "voce perdeu":
            vitorias -= 1
        else:
            vitorias += 0
        
        print(f"Seu numero de vitorias foi: {vitorias}")
            
        jogar_novamente = input("voce quer jogar novamente?").lower()
        if jogar_novamente != "sim":
            break

def define_vencedor(escolha_jogador, escolha_computador):
        if escolha_jogador == escolha_computador:
            return "empate"
        elif (
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador  == "papel")
            ):
            return "voce ganhou"
        else:
            return "voce perdeu"
        
if __name__ == "__main__":
    jogar_jokenpo()




