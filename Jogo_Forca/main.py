import adivinhacao
import forca

print("**********************************************")
print("******** Bem Vindo a central de jogos ********")
print("**********************************************")

print("(1) Adivinhacao \n (2) Forca \n\n")

jogo = int(input("Qual jogo?"))

if jogo == 1:
    adivinhacao.jogar()
elif jogo == 2:
    forca.jogar()