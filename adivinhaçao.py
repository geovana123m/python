import random
#declaracao da funcao (def)
def jogar_adivinhacao():
    
     nivel = int(input("escolha o nivel de dificuldade(1- facil, 2- medio, 3- dificil):"))
     max_numero = 10 if nivel == 1 else 50 if nivel == 2 else 100
     numero_secreto = random.randint(1, max_numero)
     tentativas = 10 if nivel == 1 else 5 if nivel == 2 else 3
     pontos = 100
     
     print(f"jogo de adivinhacao - nivel {nivel}")
     print(f"tente adivinhar o numero que estou pensando, entre 1 {max_numero}.")
     
     
     for tentativa in range(1,  tentativas + 1):
         print(f"tentativa{tentativa} de {tentativas}")
         palpite = int(input("digite seu palpite:"))
         
         if palpite < 1 or palpite > max_numero:
             print(f"digite um numero entre 1 e {max_numero}.")
             continue
         
         acertou = palpite == numero_secreto
         maior = palpite > numero_secreto
         menor = palpite < numero_secreto
         
         if acertou:
             print(f"voce acertou e fez {pontos} pontos")
             break
         else:
             pontos_perdidos = abs(numero_secreto - palpite)
             pontos -= pontos_perdidos
             if maior:
                print("seu palpite foi maior do que o numero secreto")
             elif menor:
                print("seu palpite foi menor do que o numero secreto")
        
     if not acertou:
         print(f"suas tentativas acabaram. o numero secreto era {numero_secreto}")
     print("fim do jogo")
    
if __name__ == "__main__":
    jogar_adivinhacao()