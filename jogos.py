import forca
import adivinhacao

def escolhe_jogo():
    print("\n*******************")
    print("ESCOLHA O SEU JOGO!")
    print("*******************\n")

    print("(1) Forca (2) Adivinhacao")

    while True:

        jogo = int(input("Escolha seu jogo: "))

        if(jogo == 1):
            print("\nJogando forca")
            forca.jogar()

        elif (jogo == 2):
            print("\nJogando Adivinhação")
            adivinhacao.jogar()

        else:
            print("Você deve escolher 1 ou 2\n")

if(__name__ =="__main__"):
    escolhe_jogo()
