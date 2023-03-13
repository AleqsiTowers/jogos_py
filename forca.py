import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 0
    print(letras_acertadas)

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Voce ganhou!!")
    else:
        print("Vce perdeu!!")

    print("FIM DO JOGO!")

def imprime_mensagem_abertura():
    print("\n***************************")
    print("BEM VINDO AO JOGO DA FORCA!")
    print("***************************\n")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


if(__name__ =="__main__"):
    jogar()




