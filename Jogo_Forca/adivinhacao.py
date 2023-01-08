import random

def jogar():
    print("**********************************************")
    print("****** Bem Vindo ao jogo da Adivinhação ******")
    print("**********************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print(numero_secreto)

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número etre 1 e 100: "))
        print("Voce digitou: ", str(chute))

        if chute < 1 or chute > 100:
            print("Voce deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Voce errou! O seu chute foi maior do que o numero secreto.")
            else:
                print("Voce errou! O seu chute foi menor do que o numero secreto.")

            pontos = pontos - (abs(numero_secreto - chute) * nivel)
            print("Pontuação atual: ", pontos)

    print("Fim de Jogo")

if __name__ == "__main__":
    jogar()
