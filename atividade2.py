n = int(input("digite o numero de notas: "))

soma = 0

for i in range(n):
    nota = float(input(f"digite a nota{i+1}: "))
    soma += nota

media = soma / n

print(f"a media das {n} notas é: {media:.2f}")