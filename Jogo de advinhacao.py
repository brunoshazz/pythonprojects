import random

numeroSecreto = random.randint(1, 100)
tentativas = 0

print("Bem vindo ao jogo!")
print("Advinhe um numero escolhido entre 1 a 100.")

while True:

    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1

    if palpite < numeroSecreto:

        print("O numero secreto e maior que seu palpite! Tente de novo")

    elif palpite > numeroSecreto:

        print("O numero secreto e menor que seu palpite! Tente de novo")

    else:
        print("Parabens! Voce acertou! Eu tinha pensado no {} e voce acertou em {} tentativas!".format(
            numeroSecreto, tentativas))

        break
