# ChampionsLeagueChallenge
Challenge using Sanic Framework base in Python 3 with Champions League datasets

## Champions League REST API

##### Para realização deste trabalho tenha como referência a temporada 2017-2018 da Champions League. Recomenda-se a utilização do framework Sanic ou Django REST para o desenvolvimento desta API, assim como a ferramenta Postman para a criação das requisições HTTP. Devem utilizar o Git como ferramenta da controlo de versão. 
##### Todos os recursos disponibilizados devem utilizar JSON, seja para receber ou entregar dados. As rotas podem receber um <parâmetro>. Todo parâmetro deve ser considerado como string.

# Recursos:

/api/champions-league/
Breve descrição sobre Liga dos Campeões
Maiores campeões (top 5)
Melhores marcadores de sempre (top 10)


/api/champions-league/<season>/
País que recebe a final
Campeão
Vice-campeão
/api/champions-league/<season>/teams/
Lista com todas as equipas da temporada em questão, assim como os seus respectivos nomes e países
/api/champions-league/<season>/teams/<name>/
Nome
País
Número de títulos da champions league
/api/champions-league/<season>/group-stage/
Lista dos grupos da temporada em questão com suas respectivas equipas
Considerar apenas a classificação final dos grupos
/api/champions-league/<season>/group-stage/<name>/
Considerar apenas a classificação final do grupo em questão
/api/champions-league/<season>/round-of-16/
Lista do chaveamento [Equipa 1 vs Equipa 2, ..., Equipa 15 vs Equipa 16]
/api/champions-league/<season>/round-of-16/<team1>/vs/<team2>/
Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
Equipa 1 deve ser considerada como a equipa que joga em casa.
/api/champions-league/<season>/quarter-finals/<team1>/vs/<team2>/
Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
Equipa 1 deve ser considerada como a equipa que joga em casa.
/api/champions-league/<season>/semi-finals/<team1>/vs/<team2>/
Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
Equipa 1 deve ser considerada como a equipa que joga em casa.
/api/champions-league/<season>/final/<team1>/vs/<team2>/
Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
Deve mostrar o campeão
Deve mostrar o vice-campeão
