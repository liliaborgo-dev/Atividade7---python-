'''
Questão 6: Calcular o fatorial de um número inteiro fornecido pelo usuário. 
Instruções: 
1. Peça ao usuário para digitar um número inteiro não negativo. 
2. Inicie uma variável fatorial com o valor 1. 
3. Use um laço (for ou while) que vá de 1 até o número digitado. 
4. A cada passo, multiplique a variável fatorial pelo número atual do laço. 
5. Ao final, mostre o resultado. 
 
Exemplo: 
Entrada do Usuário: 
Digite um número para calcular o fatorial: 5 
 
Saída do Programa: 
O fatorial de 5 é: 120 
(Explicação: 5! = 5 * 4 * 3 * 2 * 1 = 120) 

'''

numero = int(input("Digite um número: "))

fatorial = 1
i = 1

while i <= numero:
    fatorial *= i
    i += 1

print(f"O fatorial de {numero} é: {fatorial}")

