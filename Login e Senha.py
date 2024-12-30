"""

Exercício:

Crie um sistema de login do usuario, que corresponda ao email e senha e depois peca ao usuario para entrar na conta cadastrada

"""
from time import sleep
import os

# Define o email do usuario
usuario = input("Digite o seu email, para cadastro: ")

# Define a senha do usuario
senha = input("Digite uma senha: ")

print("Email e Senha foram cadastrados com sucesso!")
print("\n" * os.get_terminal_size().lines)

print("Seja bem vindo!")
usuarioDigitado = input("\nDigite seu email cadastrado: ")

senhaDigitada = input("\nDigite sua Senha: ")
print("\n" * os.get_terminal_size().lines)

while (usuario != usuarioDigitado):
    sleep(2)
    if senha != senhaDigitada:
        print("Email e/ou senha incorretos!")

        usuarioDigitado = input("\nDigite novamente seu email cadastrado: ")

        senhaDigitada = input("\nDigite novamente sua Senha: ")

else:
    print("Login feito com sucesso!")
