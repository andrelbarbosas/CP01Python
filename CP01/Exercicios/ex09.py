#Classificação de temperatura

temp = float(input("Digite a temperatura em graus Celsius: "))
if temp < 0:
    print("Congelante")
elif temp >= 0 and temp <= 30:
    print("Agradável")
else:
    print("Quente")
 