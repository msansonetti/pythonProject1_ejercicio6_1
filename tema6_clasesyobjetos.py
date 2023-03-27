import random


def main():
    print("TIRADA DE DADOS")
    numero = int(input("Número de dados: "))
    if numero < 1:
        print("¡Imposible!")
    else:
        print("Dados: ", end="")
        for _ in range(numero):
            print(f"{random.randrange(1, 7)} ", end="")


if __name__ == "__main__":
    main()