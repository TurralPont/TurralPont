import random
options = ["piedra", "papel", "tijeras"]
player = random.choice(options)
computer = random.choice(options)

print(f"Escogiste: {player}")
print(f"Escogió: {computer}")

if player == "piedra" and computer == "tijeras":
  print("Ganaste")
elif player == "papel" and computer == "piedra":
  print("Ganaste")
elif player == "tijeras" and computer == "papel":
  print("Ganaste")
elif player == computer:
  print("Empate")
else:
  print("Perdiste")
