try:
    n1= float(input("escreva um numero"))
    n2= float(input("escreva um segundo numero"))
except ValueError:
    print("tente novamente")
    
soma = n1 + n2

print (f"o numero {n1} mais o numero {n2} é igual a: {soma}")
