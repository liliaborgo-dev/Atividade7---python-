'''Questão 5: Solicitar uma senha ao usuário e garantir que ela tenha pelo menos 8 caracteres. 
Instruções: 
1. Inicie um laço while. 
2. Peça ao usuário para digitar uma senha. 
3. Verifique se o comprimento (length) da senha é menor que 8. 
4. Se for menor, mostre uma mensagem de erro. O laço continuará. 
5. Se tiver 8 ou mais caracteres, mostre uma mensagem de sucesso e encerre o laço. 
Exemplo: 
Entrada do Usuário: 
Crie uma senha: 1234 
Sua senha é muito curta. Tente novamente. 
Crie uma senha: abc 
Sua senha é muito curta. Tente novamente. 
Crie uma senha: senhaforte123 
Saída do Programa: 
Senha cadastrada com sucesso!'''

while True:
    senha = input("Crie uma senha: ")
    
    if len(senha) < 8:
        print("Sua senha é muito curta. Tente novamente.")
    else:
        print("Senha cadastrada com sucesso!")
        break
    