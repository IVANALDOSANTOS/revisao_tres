#Crie uma função que imprime uma contagem de 0 a 2

def contar_ate_vinte():
    
    contador = 0
    while(contador <= 20):
        print(contador)
        contador = contador + 1

contar_ate_vinte()

#*****************************
#6. Crie uma função que imprime uma contagem de 0 até o número que o usuário digitou

def print_count(n):
    for i in range(n + 1):
        print(i)

# Obter entrada do usuário
num = int(input("Digite um número: "))

# Chamar a função com a entrada do usuário
print_count(num)
