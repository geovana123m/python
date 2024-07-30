def circulo(raio):
    area = pi * (raio * raio)
    return area
raio = float(input("Digite o raio do circulo: "))
pi = 3.14
area = circulo(raio)
print(f"a area do circulo com raio {area}")