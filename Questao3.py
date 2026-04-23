'''
Questão 3: Ler 200 números inteiros e calcular a soma total dos restos da divisão de cada 
número por 3. 
Instruções: 
1. Inicie uma variável para armazenar a soma total, com o valor 0. 
2. Crie um laço que se repita 200 vezes. 
3. Dentro do laço, peça ao usuário para digitar um número. 
4. Calcule o resto da divisão deste número por 3 (usando o operador %). 
5. Adicione esse resto à soma total. 
6. Ao final do laço, exiba o valor da soma total. 

'''

'''1. variável para armazenar a soma'''
soma_total = 0

'''2. laço que se repete 200 vezes'''
for i in range(200):
    numero = int(input(f"Digite o {i + 1}º número: "))
    
    '''3. calcula o resto da divisão por 3'''
    resto = numero % 3
    
    '''4. soma o resto'''
    soma_total += resto

'''5. exibe o resultado'''
print("Soma total dos restos:", soma_total)

