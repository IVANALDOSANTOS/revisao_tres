def imprimir_nomes():

    nomes = ["João ", "Maria", "Pedro", "José"]
    print("1 " , nomes[0])
    print("2 " , nomes[1])
    print("3 " , nomes[2])
    print("4 " , nomes[3])

imprimir_nomes()  
#-------------------------------------------------------------------

def imprime_primeiro_e_ultimo_nome(nomes):
    if len(nomes) < 2:
        print("O array deve conter pelo menos dois nomes.")
        return

    print(f"O primeiro nome é: {nomes[0]}")
    print(f"O último nome é: {nomes[3]}")

# Exemplo de uso
nomes = ["João", "Maria", "Pedro", "Ana"]
imprime_primeiro_e_ultimo_nome(nomes)

#--Crie uma função que declara um array com 4 nomes
# diferentes e imprime o primeiro e último nome do array

def imprime_primeiro_e_ultimo_nome(nomes):
    if len(nomes) < 2:
        print("O array deve conter pelo menos dois nomes.")
        return

    print(f"O segundo nome é: {nomes[1]}")
    print(f"O último nome é: {nomes[2]}")

# Exemplo de uso
nomes = ["João", "Maria", "Pedro", "Ana"]
imprime_primeiro_e_ultimo_nome(nomes)