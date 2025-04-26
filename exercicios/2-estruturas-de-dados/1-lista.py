# Crie uma lista apenas com elementos numéricos
misto = [1,3,56,98,70,101]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = ['python', 72, False, 'Paloma', [1,2,3], 34, 11]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(mista [:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_misto_par = mista[::2]
print(elementos_misto_par)
# Remova da lista o último item
mista.pop()
print(mista)
# Insira na lista um novo item
mista.append('Lucas')
print(mista)
# Remova da lista um item específico
mista.remove('Paloma')
print(mista)