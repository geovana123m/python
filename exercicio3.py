nota = int(input("Digite sua nota: "))
if nota >90:
    categoria = "A"
elif nota >80:
    categoria = "B"
elif nota >70:
    categoria = "C"
elif nota >60:
    categoria = "D"
else:
    categoria = "F"
print(f"Você está na categoria: {categoria}.")