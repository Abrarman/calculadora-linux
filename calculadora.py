print("Calculadora Lógica")

while True:
    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Menu de operações
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Comparação")
    print("7 - Paridade")
    print("8 - Sair")

    escolha = input("Digite o número da operação: ")

    # Soma
    if escolha == "1":
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")

    # Subtração
    elif escolha == "2":
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")

    # Multiplicação
    elif escolha == "3":
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")

    # Divisão
    elif escolha == "4":
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: divisão por zero!")

    # Potência
    elif escolha == "5":
        print(f"Resultado: {num1} ** {num2} = {num1 ** num2}")

    # Comparação
    elif escolha == "6":
        if num1 > num2:
            print(f"{num1} é maior e {num2} é menor")
        elif num1 < num2:
            print(f"{num1} é menor e {num2} é maior")
        else:
            print(f"{num1} e {num2} são iguais")

    # Paridade
    elif escolha == "7":
        if num1 % 2 == 0:
            print(f"{num1} é par")
        else:
            print(f"{num1} é ímpar")

        if num2 % 2 == 0:
            print(f"{num2} é par")
        else:
            print(f"{num2} é ímpar")

    # Saída
    elif escolha == "8":
        break
    else:
        print("Opção inválida, tente novamente.")

    print("\n---\n")

   # Pergunta se quer continuar
    continuar = input("\nDeseja Continuar? (s/n): ").lower()
    if continuar != 's':
        print("Bons estudos e até mais. Encerrando!")
        break
