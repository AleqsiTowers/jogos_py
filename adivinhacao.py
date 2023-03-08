import random

def jogar():

    print("\n*********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("*********************************\n")

    jogar_novamente = True

    while jogar_novamente == True:
        numero_secreto = random.randrange(1, 101)
        total_de_tentativas = 0
        pontos = 1000

        print("Qual nível de dificuldade você deseja?\n")
        print("(1) - Fácil (2) - Médio (3) - Difícil")

        while True:
            nivel = int(input("Defina o nível: "))

            if (nivel == 1):
                total_de_tentativas = 20
                break
            elif (nivel == 2):
                total_de_tentativas = 10
                break
            elif (nivel == 3):
                total_de_tentativas = 5
                break
            else:
                print("Você deve digitar um valor de 1 a 3.\n")

        for rodada in range(1, total_de_tentativas + 1):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))

            chute_str = input("Digite um número entre 1 e 100: ")
            print("Você digitou", chute_str, "")
            chute = int(chute_str)

            if (chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 100!!")
                continue

            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print("Você acertou e fez {} pontos!\n".format(pontos))
                break
            else:
                if (maior):
                    print("Você errou! O seu chute foi maior do que o número secreto.\n")
                elif (menor):
                    print("Você errou! O seu chute foi menor do que o número secreto.\n")

                pontos_perdidos = abs(numero_secreto - chute)
                pontos -= pontos_perdidos

        if not acertou:
            print("O número secreto era {}.".format(numero_secreto))

        while True:
            jogar_novamente = input("Deseja jogar novamente? (S/N) ").lower()

            if jogar_novamente == "n":
                jogar_novamente = False
                print("FIM DO JOGO!!")
                break
            elif jogar_novamente == "s":
                print("Vamos jogar novamente!")
                jogar_novamente = True
                break
            else:
                print("Opção inválida! Digite S para jogar novamente ou N para encerrar o jogo.")
                continue


if(__name__ == "__main__"):
    jogar()