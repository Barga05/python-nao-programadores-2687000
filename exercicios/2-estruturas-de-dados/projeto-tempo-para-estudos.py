# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome =input('Qual seu nome?')
total_dias = input('Total de dias dedicados ao estudo durante a semana?')
total_horas = input('Média de horas estudada por dia?')
curso = input('Qual curso desejado?')
total_horas = int(total_horas)
total_dias = int(total_dias)
print(f'Olá {nome}, você costuma estudar {total_dias} dias por semana, durante mais ou menos {total_horas} horas diárias. isso significa que você estuda em média {total_dias*total_horas}horas para o curso {curso}')