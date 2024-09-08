import random

numero_secreto = random.randint(1,100)

tentativa = 1

while True:
  chute = int(input(f"Tentativa{tentativa}: Digite um número: "))

  if chute == numero_secreto:
    print("Parabéns! Você acertou")
    break
  
  elif chute < numero_secreto:
    print("O número secreto é maior que o seu chute.")

  else:
    print("O número secreto é menor que o seu chute.")

  tentativa += 1
  