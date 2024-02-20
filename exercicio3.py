mes =input("digite um mes do ano")
if mes in ("dezembro", "janeiro", "fevereiro"):
    categoria = "verao"
if mes in ("março", "abril", "maio"):
        categoria = "outono"
if mes in("junho", "julho","agosto"):
    categoria = "inverno"
if mes in("setembro", "outubro", "novembro"):
    categoria = "primavera"
print(f"a estaçao do seu mes é: {categoria}")