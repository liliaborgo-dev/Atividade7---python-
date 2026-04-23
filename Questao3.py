# 1. variável para armazenar a soma
soma_total = 0

# 2. laço que se repete 200 vezes
for i in range(200):
    numero = int(input(f"Digite o {i + 1}º número: "))
    
    # 3. calcula o resto da divisão por 3
    resto = numero % 3
    
    # 4. soma o resto
    soma_total += resto

# 5. exibe o resultado
print("Soma total dos restos:", soma_total)

