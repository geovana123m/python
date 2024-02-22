import random

numero_secreto = random.randint(1,10)
tentativas = 0
max_tentativas = 5


while tentativas < max_tentativas:
    palpite = int(input("digite seu  palpite"))
    tentativas +=  1
    if palpite == numero_secreto:
        print(f"parabens, voce acertou")
        break
    elif palpite > numero_secreto:
        print(f"tente um numero menor")
    else:
        print(f"tente um numero maior")
        
    if tentativas < max_tentativas:
        print(f"voce tem {max_tentativas - tentativas} tentativas")
    else:
        print(f"voce nao acertou o numero era {numero_secreto}")
        
print("fim de jogo")    
