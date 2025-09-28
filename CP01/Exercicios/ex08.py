#Par, Multiplo de 5 ou Outro número

num = int(input("Digite um número interio: "))
if num % 2 == 0:
    print("Par")
elif num % 5 == 0:
    print("Multiplo de 5")
else:
    print("Outro número.")