import random

def jogar():
    jogar_novamente = True

    while jogar_novamente == True:
        imprime_mensagem_abertura()
        palavra_secreta = carrega_palavra_secreta()

        letras_acertadas = ["_" for letra in palavra_secreta]
        letras_erradas = []
        erros = 0
        print(letras_acertadas)

        enforcou = False
        acertou = False

        while (not enforcou and not acertou):

            chute = pede_chute()

            if (chute in palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
            else:
                if(chute not in palavra_secreta):
                    letras_erradas.append(chute)
                erros += 1
                desenha_forca(erros)
            print("\nVocê errou {} de 7 vezes possíveis.".format(erros))
            print("Letras que você errou: {}".format(letras_erradas))

            enforcou = erros == 7
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)

        if (acertou):
            print("Parabéns, você ganhou!\n")
        else:
            print("Puxa, você foi enforcado!")
            print("A palavra era {}".format(palavra_secreta))
        while True:
            jogar_novamente = input("Deseja jogar novamente? (S/N)").lower()

            if jogar_novamente == "n":
                jogar_novamente = False
                print("FIM DO JOGO!")
                break

            elif jogar_novamente == "s":
                print("Vamos jogar novamente!")
                jogar_novamente = True
                break
            else:
                print("Opção inválida, digite S ou N!")


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

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ =="__main__"):
    jogar()




