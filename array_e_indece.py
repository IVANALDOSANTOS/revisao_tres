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

#Crie uma função que pede 3 nomes de alimentos digitado pelo usuário e substitui
# os elementos do array [“Macarrão”, “Pepino”, “Batata”] 
#com esses 3 alimentos. Imprima o nome dos alimentos um abaixo do outro.

def atualiza_e_imprime_nomes_de_alimentos():
    # Declara o array com os nomes de alimentos
    alimentos = ["Macarrão", "Pepino", "Batata"]

    # Pede ao usuário que digite 3 nomes de alimentos
    for i in range(3):
        alimento = input(f"Digite o nome do alimento {i+1}: ")
        # Substitui os elementos do array com os novos nomes de alimentos
        alimentos[i] = alimento

    # Imprime o nome dos alimentos um abaixo do outro
    for alimento in alimentos:
        print(alimento)

# Chama a função
atualiza_e_imprime_nomes_de_alimentos()