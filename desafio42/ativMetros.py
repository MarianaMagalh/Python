def converter(centimetros):
    converter = centimetros / 100
    return converter

centimetros = int(input("Digite um valor: "))

converter = converter(centimetros)

print(f"O resultado da converção é {converter}")

