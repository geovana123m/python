def calcArea(base,altura):
    area = (base * altura) / 2
    return area

base = float(input("digite a base"))
altura = float(input("digite a altura"))
area = calcArea(base,altura)
print(f"a area do quadrado é {area}")