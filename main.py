import sys

# Cria uma função para executar o programa principal
def main():
    print(f"Dados Enviados: {sys.argv[0]}")
    print(f"Arg enviados: {sys.argv}")


# Verifica se o programa é o principal
if __name__ == "__main__":
    main()