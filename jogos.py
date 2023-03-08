import forca
import adivinhacao

def escolhe_jogo():
    print("\n*******************")
    print("ESCOLHA O SEU JOGO!")
    print("*******************\n")

    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Escolha seu jogo: "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("\nJogando Adivinhação")
        adivinhacao.jogar()

if(__name__ =="__main__"):
    escolhe_jogo()
