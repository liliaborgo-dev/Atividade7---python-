n = 1
soma = 0

numero = int(input("Digite um número inteiro positivo: "))

while n <= numero:
    soma += n
    n += 1

print(f"A soma de 1 até {numero} é: {soma}")
