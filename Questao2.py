'''
Questão 2: Calcular a soma de todos os números inteiros de 1 até um número escolhido pelo 
usuário. 
Instruções: 
1. Peça ao usuário para digitar um número inteiro positivo. 
2. Use um laço while para somar todos os números de 1 até o número digitado. 
3. Mostre o resultado final da soma. 
 
Exemplo: 
Entrada do Usuário: 
Digite um número: 5 
 
Saída do Programa: 
A soma de 1 até 5 é: 15

'''



n = 1
soma = 0

numero = int(input("Digite um número inteiro positivo: "))

while n <= numero:
    soma += n
    n += 1

print(f"A soma de 1 até {numero} é: {soma}")
