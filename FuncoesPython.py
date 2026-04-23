# len() → tamanho
texto = "python"
print(len(texto))  # 6

# int() → inteiro
numero = int("10")
print(numero + 5)  # 15

# float() → decimal
valor = float("10.5")
print(valor)  # 10.5

# str() → texto
idade = 20
print("Idade: " + str(idade))

# input() → entrada
nome = input("Digite seu nome: ")
print(nome)

# print() → saída
print("Olá mundo")

# range() → repetição
for i in range(5):
    print(i)  # 0 até 4

# type() → tipo
x = 10
print(type(x))  # <class 'int'>

# ⚠️ input sempre retorna texto
numero = input("Digite um número: ")      # errado para cálculo
numero = int(input("Digite um número: ")) # correto

'''
git add .
git commit -m "exercicio pronto"
git push

'''