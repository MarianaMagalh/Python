def area(base, altura):
    area = base * altura
    return area

print("Area do Retangulo")

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area = area(base, altura)

print(f"A area do retangulo é de {area}")