import random

def jogar_caça_níqueis(aposta):
    # Define as probabilidades de ganho para os jogadores
    chances_de_ganho = 0.28

    # Simula o resultado do jogo
    resultado = random.random()  # Gera um número aleatório entre 0 e 1

    # Verifica se o jogador ganhou ou perdeu
    if resultado < chances_de_ganho:
        # O jogador ganhou
        premio = aposta * 2  # Prêmio é o dobro da aposta
        print("Parabéns! Você ganhou {}!".format(premio))
        return premio
    else:
        # A casa ganhou
        premio = 0  # O jogador não ganha nada
        print("Você perdeu. Tente novamente!")
        return premio

def main():
    saldo = float(input("Digite seu saldo: "))# Saldo inicial do jogador

    while saldo > 0:
        print("\nSeu saldo atual é de ${}".format(saldo))
        aposta = int(input("Quanto você quer apostar? (0 para sair): "))

        if aposta == 0:
            print("Obrigado por jogar! Até a próxima.")
            break

        if aposta > saldo:
            print("Você não tem saldo suficiente para fazer essa aposta.")
            continue

        saldo -= aposta  # Subtrai a aposta do saldo do jogador
        premio = jogar_caça_níqueis(aposta)
        saldo += premio  # Adiciona o prêmio ao saldo do jogador

    print("Seu saldo acabou. Volte em breve!")

if __name__ == "__main__":
    main()