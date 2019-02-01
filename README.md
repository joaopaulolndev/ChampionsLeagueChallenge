


<p align="center">
  <a href="https://github.com/joaopaulolndev/">
    <img alt="" src="https://nssdata.s3.amazonaws.com/images/galleries/16702/uefa-champions-league-rebranding-2018-2021-7.jpg">
  </a>
</p>

## About Champions League REST API Challenge:

<p>Desafio Champions league, using <b>Python 3</b> and <b>Sanic Framework</b>.</p>
<p>Champions League Challenge, using <b>Python 3</b> and <b>Sanic Framework</b>.</p>

<p>Para realização deste trabalho tenha como referência a temporada <b>2017-2018 da Champions League</b>. 
Recomenda-se a utilização do framework <b>Sanic</b> ou <b>Django REST</b> para o desenvolvimento desta API, assim como a ferramenta <b>Postman</b> para a criação das requisições HTTP. 
Devem utilizar o <b>Git</b> como ferramenta da controlo de versão.</p> 

<p>For the accomplishment of this work reference has been made to the <b>2017-2018 season of the Champions League</b>.
It is recommended to use the <b>Sanic</b> or <b>Django REST</b> framework for the development of this API, as well as the <b>Postman</b> tool for the creation of HTTP requests.
They should use <b>Git</b> as a version control tool.</p>

<p>Todos os recursos disponibilizados devem utilizar <b>JSON</b>, seja para receber ou entregar dados. 
As rotas podem receber um &lt;parâmetro&gt;. 
Todo parâmetro deve ser considerado como string.</p>

<p> All available resources must use <b>JSON</b>, either to receive or deliver data.
Routes can receive a &lt;parameter&gt;.
Every parameter must be considered as a string.
</p>

## Requirements:
   * Python 3.6
   * Sanic Framework 18.12
   
<p align="center">
  <img alt="" src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg">
  <img src="https://img.shields.io/badge/size-465%20kB-green.svg" alt="">
  <img src="https://img.shields.io/badge/license-MIT-000.svg" alt="">
  <img src="https://img.shields.io/badge/Sanic%20Framework-18.12-red.svg" alt="">
  <img src="https://img.shields.io/badge/platform-linux--64%20%7C%20win--32%20%7C%20osx--64%20%7C%20win--64-lightgrey.svg" alt="">
</p>
   
## Installing Sanic Framework

Installing `sanic` from the `pip`

```
pip3 install sanic
```

Installing `sanic` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
```

Once the `conda-forge` channel has been enabled, `sanic` can be installed with:

```
conda install sanic
```

It is possible to list all of the versions of `sanic` available on your platform with:

```
conda search sanic --channel conda-forge
```
    
## Run Instructions:
    Run this code local > python3 main.py 
    Open the Browser http://0.0.0.0:8000
       

## Build:

   Pode visualizar a aplicação nesse endereço. <br/>
   You can view the application at this address.

   [https://champions-league-challenge.herokuapp.com/api/champions-league/](https://champions-league-challenge.herokuapp.com/api/champions-league/)

## Resources:

* 1 /api/champions-league/
    + Breve descrição sobre Liga dos Campeões
    + Maiores campeões (top 5)
    + Melhores marcadores de sempre (top 10) 
    <br /><br />
    + Short description about Champions League
    + Top Champions (top 5)
    + Best scorer (top 10)
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league](https://champions-league-challenge.herokuapp.com/api/champions-league)
    
* 2 /api/champions-league/&lt;season&gt;/
    + País que recebe a final
    + Campeão
    + Vice-Campeão 
    <br /><br />
    + Country that receives the final
    + Champion
    + Runners-up
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18)
    
* 3 /api/champions-league/&lt;season&gt;/teams/
    + Lista com todas as equipas da temporada em questão, assim como os seus respectivos nomes e países
    <br /><br /> 
    + List with all the teams of the season in question, as well as their respective names and countries
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/teams/](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/teams/)

* 4 /api/champions-league/&lt;season&gt;/teams/&lt;name&gt;/
    + Nome
    + País
    + Número de títulos da liga dos campeões
    <br/><br/>
    + Name
    + Country
    + Number of Champions League Titles
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/teams/madrid](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/teams/madrid)
  
 * 5 /api/champions-league/&lt;season&gt;/group-stage/   
    + Lista dos grupos da temporada em questão com suas respectivas equipas
    + Considerar apenas a classificação final dos grupos
    <br/><br/>
    + List of groups of the season in question with their respective teams
    + Consider only the final classification of groups
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/group-stage](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/group-stage)
    
* 6 /api/champions-league/&lt;season&gt;/group-stage/&lt;name&gt;/
    + Considerar apenas a classificação final do grupo em questão
    <br/><br/>
    + Consider only the final classification of the group in question
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/group-stage/A/](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/group-stage/A)

    
* 7 /api/champions-league/&lt;season&gt;/round-of-16/      
    + Lista do chaveamento [Equipa 1 vs Equipa 2, ..., Equipa 15 vs Equipa 16]
    <br/><br/>
    + Match lists [Team 1 vs Team 2, ..., Team 15 vs Team 16]
    
      Example : [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/round-of-16](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/round-of-16) 
    
* 8 /api/champions-league/&lt;season&gt;/round-of-16/&lt;team1&gt;/vs/&lt;team2&gt;/ 
    +  Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    +  Equipa 1 deve ser considerada como a equipa que joga em casa.
    <br/></br>
    + Should be the result of the match between Team 1 vs Team 2.
    + Team 1 should be considered as the team that plays at home.
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/round-of-16/juventus/vs/tottenham](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/round-of-16/juventus/vs/tottenham)
     
* 9 /api/champions-league/&lt;season&gt;/quarter-finals/&lt;team1&gt;/vs/&lt;team2&gt;/  
    + Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    + Equipa 1 deve ser considerada como a equipa que joga em casa.
    <br/><br/>
    + Should be the result of the match between Team 1 vs Team 2.
    + Team 1 should be considered as the team that plays at home.
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/quarter-finals/barcelona/vs/roma](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/quarter-finals/barcelona/vs/roma)
    
* 10 /api/champions-league/&lt;season&gt;/semi-finals/&lt;team1&gt;/vs/&lt;team2&gt;/
    + Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    + Equipa 1 deve ser considerada como a equipa que joga em casa.
    <br/><br/>
    + Should be the result of the match between Team 1 vs Team 2.
    + Team 1 should be considered as the team that plays at home.  
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/semi-finals/liverpool/vs/roma](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/semi-finals/liverpool/vs/roma)

* 11 /api/champions-league/&lt;team1&gt;/final/&lt;team1&gt;/vs/&lt;team2&gt;/
    + Deve mostrar o resultado da partida entre Equipa 1 vs Equipa 2.
    + Deve mostrar o campeão
    + Deve mostrar o campeão
    <br/></br>
    + Should be the result of the match between Team 1 vs Team 2.
    + Show the Champion
    + Show the Runner-up
    
      Example: [https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/final/madrid/vs/liverpool](https://champions-league-challenge.herokuapp.com/api/champions-league/2017-18/final/madrid/vs/liverpool)
  
## Parameters:
   >Segue a documentação sobre utilização dos parametros das requisições
   <br/> Follow the documentation about use parameters of requisitions
   
   * &lt;season&gt; : 2016-17, 2017-18...
   * group-stage/&lt;season&gt;/ : A, B, C, D, E, F, G, H
   * &lt;team1&gt; and &lt;team2&gt; : use somente a key do time / use only the team key : <br/>
   anderlecht, feyenoord, porto, benfica, sportinglisboa, cskamoskva, spartak, celtic,
   besiktas, donezk, maribor, qarabag, olympiacos, apoel, barcelona, liverpool, bayern,
   dortmund, leipzig, chelsea, tottenham, manutd, mancity, madrid, atletico, sevilla,
   roma, juventus, napoli, paris, monaco, basel
   
## Patterns 
Utilizado para boas práticas de programação em Python o 
[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) como referência.

Used for good programming practice in Python the [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) as a reference.   
    
## References:

   - [Sanic Framework Documentation](https://sanic.readthedocs.io/en/latest/index.html)
   - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
   - [Sanic Feedstock](https://github.com/conda-forge/sanic-feedstock)
   - [UEFA Champions League Wikipedia](https://en.wikipedia.org/wiki/UEFA_Champions_League)
   - [2017–18 UEFA Champions League](https://en.wikipedia.org/wiki/2017%E2%80%9318_UEFA_Champions_League)
   - [2016–17 UEFA Champions League](https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League)
   - [Open Football](https://github.com/openfootball/football.json)
   - [Postman](https://www.getpostman.com/)
   - [Git](https://git-scm.com/)
   - [PyCharm](https://www.jetbrains.com/pycharm/)
   - [Shields IO](https://shields.io/#/)

