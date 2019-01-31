


<p align="center">
  <a href="https://github.com/joaopaulolndev/">
    <img alt="" src="https://nssdata.s3.amazonaws.com/images/galleries/16702/uefa-champions-league-rebranding-2018-2021-7.jpg">
  </a>
</p>

## About Champions League REST API Challenge:

<p>Desafio Champions league, using Python 3 and Sanic Framework.</p>
<p>Champions League Challenge, using Python 3 and Sanic Framework.</p>

<p>Para realização deste trabalho tenha como referência a temporada 2017-2018 da Champions League. 
Recomenda-se a utilização do framework Sanic ou Django REST para o desenvolvimento desta API, assim como a ferramenta Postman para a criação das requisições HTTP. 
Devem utilizar o Git como ferramenta da controlo de versão.</p> 

<p>For the accomplishment of this work reference has been made to the 2017-2018 season of the Champions League.
It is recommended to use the Sanic or Django REST framework for the development of this API, as well as the Postman tool for the creation of HTTP requests.
They should use Git as a version control tool.</p>

<p>Todos os recursos disponibilizados devem utilizar JSON, seja para receber ou entregar dados. 
As rotas podem receber um <parâmetro>. 
Todo parâmetro deve ser considerado como string.</p>

<p> All available resources must use JSON, either to receive or deliver data.
Routes can receive a <parameter>.
Every parameter must be considered as a string.
</p>

## Requirements:
   * Python >= 3.5+
   * Sanic Framework 18.12
    
<p align="center">
  <img alt="" src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg">
  <img src="https://img.shields.io/badge/size-465%20kB-green.svg" alt="">
  <img src="https://img.shields.io/badge/license-MIT-000.svg" alt="">
  <img src="https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg" alt="">
  <img src="https://img.shields.io/badge/Sanic%20Framework-18.12-red.svg" alt="">
</p>

## Run:
    Run this code > python3 main.py 
    Open the Browser http://0.0.0.0:8000
       

## Resources:

* 1 /api/champions-league/
    + Breve descrição sobre Liga dos Campeões
    + Maiores campeões (top 5)
    + Melhores marcadores de sempre (top 10) 
    <br /><br />
    + Short description about Champions League
    + Top Champions (top 5)
    + Best scorer (top 10)
    
* 2 /api/champions-league/&lt;season&gt;/
    + País que recebe a final
    + Campeão
    + Vice-Campeão 
    <br /><br />
    + Country that receives the final
    + Champion
    + Runners-up
    
* 3 /api/champions-league/&lt;season&gt;/teams/
    + Lista com todas as equipas da temporada em questão, assim como os seus respectivos nomes e países
    <br /><br /> 
    + List with all the teams of the season in question, as well as their respective names and countries

* 4 /api/champions-league/&lt;season&gt;/teams/&lt;name&gt;/
    + Nome
    + País
    + Número de títulos da liga dos campeões
    <br/><br/>
    + Name
    + Country
    + Number of Champions League Titles
  
 * 5 /api/champions-league/&lt;season&gt;/group-stage/   
    + Lista dos grupos da temporada em questão com suas respectivas equipas
    + Considerar apenas a classificação final dos grupos
    <br/><br/>
    + List of groups of the season in question with their respective teams
    + Consider only the final classification of groups
    
* 6 /api/champions-league/&lt;season&gt;/group-stage/&lt;name&gt;/
    + Considerar apenas a classificação final do grupo em questão
    <br/><br/>
    + Consider only the final classification of the group in question
    
* 7 /api/champions-league/&lt;season&gt;/round-of-16/      
    + Lista do chaveamento [Equipa 1 vs Equipa 2, ..., Equipa 15 vs Equipa 16]
    <br/><br/>
    + Match lists [Team 1 vs Team 2, ..., Team 15 vs Team 16]  
    
* 8 /api/champions-league/&lt;season&gt;/round-of-16/&lt;team1&gt;/vs/&lt;team2&gt;/ 
    +  Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    +  Equipa 1 deve ser considerada como a equipa que joga em casa.
    <br/></br>
    + Should be the result of the match between Team 1 vs Team 2.
    + Team 1 should be considered as the team that plays at home. 
     
* 9 /api/champions-league/&lt;season&gt;/quarter-finals/&lt;team1&gt;/vs/&lt;team2&gt;/  
    + Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    + Equipa 1 deve ser considerada como a equipa que joga em casa.
    <br/><br/>
    + Should be the result of the match between Team 1 vs Team 2.
    + Team 1 should be considered as the team that plays at home.
    
* 10 /api/champions-league/&lt;season&gt;/semi-finals/&lt;team1&gt;/vs/&lt;team2&gt;/
    + Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    + Equipa 1 deve ser considerada como a equipa que joga em casa.
    <br/><br/>
    + Should be the result of the match between Team 1 vs Team 2.
    + Team 1 should be considered as the team that plays at home.  

* 11 /api/champions-league/&lt;team1&gt;/final/&lt;team1&gt;/vs/&lt;team2&gt;/
    + Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    + Deve mostrar o campeão
    + Deve mostrar o campeão
    <br/></br>
    + Should be the result of the match between Team 1 vs Team 2.
    + Show the Champion
    + Show the Runner-up
  
## Parameters:
   >Segue a documentação sobre utilização dos parametros das requisições
   <br/> Follow the documentation about use parameters of requisitions
   
   * &lt;season&gt; : 2016-17, 2017-28...
   * group-stage/&lt;season&gt;/ : A, B, C, D, E, F, G, H
   * &lt;team1&gt; and &lt;team2&gt; : use somente a key do time / use only the team key : <br/>
   anderlecht, feyenoord, porto, benfica, sportinglisboa, cskamoskva, spartak, celtic,
   besiktas, donezk, maribor, qarabag, olympiacos, apoel, barcelona, liverpool, bayern,
   dortmund, leipzig, chelsea, tottenham, manutd, mancity, madrid, atletico, sevilla,
   roma, juventus, napoli, paris, monaco, basel
    
## References:

   - [Sanic Framework Documentation](https://sanic.readthedocs.io/en/latest/index.html)
   - [UEFA Champions League Wikipedia](https://en.wikipedia.org/wiki/UEFA_Champions_League)
   - [2017–18 UEFA Champions League](https://en.wikipedia.org/wiki/2017%E2%80%9318_UEFA_Champions_League)
   - [2016–17 UEFA Champions League](https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League)
   - [Open Football](https://github.com/openfootball/football.json)
   - [Postman](https://www.getpostman.com/)
   - [Git](https://git-scm.com/)
   - [PyCharm](https://www.jetbrains.com/pycharm/)
   - [Shields IO](https://shields.io/#/)

