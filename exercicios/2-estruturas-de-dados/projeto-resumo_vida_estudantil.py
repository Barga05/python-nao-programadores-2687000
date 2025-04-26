# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante ['nome'] = input('Qual seu nome?')
estudante ['ano_que_conheceu_o_linkedin'] = int(input('Qual ano conheceu o Linkedin?'))
estudante ['ano_atual'] = int(input ('Qual o ano atual?'))
curso = input('Quais cursos realizou no Linkedin Learning?')

estudante ['curso'] = curso.split(', ')


# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante ['ano_atual'] - estudante ['ano_que_conheceu_o_linkedin']
total_cursos = len(estudante['curso'])

print(f"Oi {estudante['nome']}, desde {estudante['ano_que_conheceu_o_linkedin']} você conhece o linkedin. Nesse {'total_anos'}, você fez {'total_cursos'}, sendo ele o primeiro curso {estudante['curso'][0]} e sendo o ultimo {estudante['curso'][-1]} ")