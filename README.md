# ChampionsLeagueChallenge
Challenge using Sanic Framework base in Python 3 with Champions League datasets

## Champions League REST API

##### Para realização deste trabalho tenha como referência a temporada 2017-2018 da Champions League. Recomenda-se a utilização do framework Sanic ou Django REST para o desenvolvimento desta API, assim como a ferramenta Postman para a criação das requisições HTTP. Devem utilizar o Git como ferramenta da controlo de versão. 
##### Todos os recursos disponibilizados devem utilizar JSON, seja para receber ou entregar dados. As rotas podem receber um <parâmetro>. Todo parâmetro deve ser considerado como string.

## Recursos:

-<b>1. /api/champions-league/</b>
<br />Breve descrição sobre Liga dos Campeões
<br />Maiores campeões (top 5)
<br />Melhores marcadores de sempre (top 10)
<br />
-<b>2. /api/champions-league/:season/</b>
<br />País que recebe a final
<br />Campeão
<br />Vice-campeão
<br />
-<b>3. /api/champions-league/:season/teams/</b>
<br />Lista com todas as equipas da temporada em questão, assim como os seus respectivos nomes e países
<br />
-<b>4. /api/champions-league/:season/teams/:name/</b> 
<br />Nome
<br />País
<br />Número de títulos da champions league 
<br /> 
-<b>5. /api/champions-league/:season/group-stage/</b> 
<br/>Lista dos grupos da temporada em questão com suas respectivas equipas
<br/>Considerar apenas a classificação final dos grupos
<br/>
-<b>6. /api/champions-league/:season/group-stage/<name>/</b> 
<br/> Considerar apenas a classificação final do grupo em questão
<br /> 
-<b>7. /api/champions-league/:season/round-of-16/</b> 
<br> Lista do chaveamento [Equipa 1 vs Equipa 2, ..., Equipa 15 vs Equipa 16]
<br>  
-<b>8. /api/champions-league/<season>/round-of-16/:team1/vs/:team2/</b>  
<br/>Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
<br/>Equipa 1 deve ser considerada como a equipa que joga em casa.
<br />
-<b>9. /api/champions-league/:season/quarter-finals/:team1/vs/:team2/</b>  
<br />Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
<br />Equipa 1 deve ser considerada como a equipa que joga em casa.
<br />
-<b>10. /api/champions-league/:season/semi-finals/:team1/vs/:team2/</b>  
<br />Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
<br>Equipa 1 deve ser considerada como a equipa que joga em casa.
<br />
-<b>11. /api/champions-league/:season/final/:team1/vs/:team/</b>  
<br />Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2. 
<br />Deve mostrar o campeão
<br>Deve mostrar o vice-campeão
  




