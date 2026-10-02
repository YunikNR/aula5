def circulo():
    raio = float(input("Qual é o raio? "))
    resultado = raio*raio*3.14
    print(f"A área é: {resultado}")

def triangulo():
    base = float(input("Qual é a base? "))
    altura = float(input("Qual é a altura? "))
    resultado = (base*altura)/2
    print(f"A área é: {resultado}")

def quadrado():
    lado = float(input("Qual é o valor do lado? "))
    resultado = lado*lado
    print(f"A área é: {resultado}")

def retangulo():
    lado1 = float(input("Qual é o primeiro lado? "))
    lado2 = float(input("Qual é o segundo lado? "))
    resultado = lado1*lado2
    print(f"A área é: {resultado}")

def paralelogramo():
    base = float(input("Qual é a base? "))
    altura = float(input("Qual é a altura? "))
    resultado = base*altura
    print(f"A área é: {resultado}")

def losango():
    lado = float(input("Qual é o valor do lado? "))
    altura = float(input("Qual é a altura? "))
    resultado = lado*altura
    print(f"A área é: {resultado}")

def trapezio():
    base1 = float(input("Qual é a base menor? "))
    base2 = float(input("Qual é a base maior? "))
    altura = float(input("Qual é a altura? "))
    resultado = ((base1+base2)*altura)/2
    print(f"A área é: {resultado}")

while True:
    print("Calculadora de Área")
    print("1 - Circulo")
    print("2 - Triângulo")
    print("3 - Quadrado")
    print("4 - Retangulo")
    print("5 - Paralelogramo")
    print("6 - Losango")
    print("7 - Trapézio")
    print("8 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        circulo()
    elif opcao == 2:
        triangulo()
    elif opcao == 3:
        quadrado()
    elif opcao == 4:
        retangulo()
    elif opcao == 5:
        paralelogramo()
    elif opcao == 6:
        losango()
    elif opcao == 7:
        trapezio()
    elif opcao == 8:
        print("Saindo do sistema...")
        exit()
    else:
        print("Opção inválida, tente novamente...")