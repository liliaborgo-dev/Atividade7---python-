'''
Questão 4: Calcular a média de vários números digitados pelo usuário. O programa deve parar 
de pedir números quando o usuário digitar -1. 
Instruções: 
1. Crie variáveis para guardar a soma e a quantidade de números digitados. 
2. Inicie um laço infinito (while True). 
3. Peça um número ao usuário. 
4. Se o número for -1, pare o laço (use break). 
5. Caso contrário, adicione o número à soma e aumente a quantidade em 1. 
6. Após o laço, calcule a média (soma / quantidade) e mostre o resultado. 
Exemplo: 
Entrada do Usuário: 
Digite um número (ou -1 para sair): 10 
Digite um número (ou -1 para sair): 20 
Digite um número (ou -1 para sair): 60 
Digite um número (ou -1 para sair): -1 
Saída do Programa: 
A média dos números digitados é: 30.0

'''

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número (ou -1 para sair): "))
    
    if numero == -1:
        break
    
    soma += numero
    quantidade += 1

media = soma / quantidade
print("A média dos números digitados é:", media)
