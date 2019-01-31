__author__ = "João Paulo Leite Nascimento"
__date__ = "31 January 2019"
__email__ = "joaopauloln7@gmail.com"

import json
import os.path

"""
" model ChampionsLeagueModel
"""
class ChampionsLeagueModel:

    """
    " Metodo com descricao sobre a liga dos campeões, maiores vencedores e maiores artilheiros
    """
    def getAbout(self):

        json_data = open('data/champions-league.json').read()
        data = json.loads(json_data)
        return data

    """
    " Metodo retorno o pais que recebeu a final, o time campeão e o vice
    """
    def getAboutBySeason(season):

        json_data = open('data/finals.json').read()
        data = json.loads(json_data)

        if (season in data['finals']):
            ret = data['finals'][season]
        else:
            raise Exception('Season not found')

        return ret

    """
    " Metodo que recupera todos os times da temporada com as suas informacoes
    """
    def getAllTeams(season):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        # recupera os dados do dataset
        json_data = open('data/' + season + '/cl.clubs.json').read()
        return json.loads(json_data)

    """
    " Metodo que recupera somente um pais com a quantidade de titulos, país de origem
    """
    def getOneTeam(season, name):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        # recupera os dados do dataset
        json_data = open('data/' + season + '/cl.clubs.json').read()
        data = json.loads(json_data)

        # executa o filter com lambda somente para recuperar o nó que está o time pesquisado
        output = list(filter(lambda x: x['key'].lower() == name.lower(), data['clubs']))

        return output[0]

    """
    " Metodo que recupera todos os grupos da temporada
    """
    def getGroups(season, group=None):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        # recupera os dados do dataset
        json_data = open('data/' + season + '/cl.groups.json').read()
        data = json.loads(json_data)

        # faz um loop para montar o chaveamento dos grupos
        result = dict()
        for i in range(0, 8):
            result[data['groups'][i]['name']] = sorted(data['groups'][i]['teams'], key=lambda x: x['position'])

        # verifica se foi passado o grupo por parametro, caso tenha passado retorna somente o grupo
        if group is not None:
            group = 'Group ' + group.upper()
            return result[group]

        return result

    """
    " Metodo para classificar as partidas das oitavas de final
    """
    def getRound16(season):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        # recupera os dados do dataset
        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        # recupera somente os jogos das oitavas de final
        matches = data['rounds'][6]['matches']

        # faz um loop para montar o chaveamento das oitavas de final
        games = dict()
        for i in range(0, len(matches)):
            games['Match ' + str(i + 1)] = str(matches[i]['team1']['name']) + " vs " + str(matches[i]['team2']['name'])

        return games

    """
    " Metodo para criacao dos playoffs das oitavas de final as semi finais
    """
    def getPlayoffs(season, team1, team2, step):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        # recupera os dados do dataset
        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        # verifica qual é a fase ao qual está sendo feita a consulta para recuperar os rounds
        if step == 'round-of-16':
            round1, round2 = 6, 7
        elif step == 'quarter-finals':
            round1, round2 = 8, 9
        elif step == 'semi-finals':
            round1, round2 = 10, 11

        # faz chamada ao metodo que monta as partidas
        game = ChampionsLeagueModel.mountGamePlayoffs(data, team1, team2, round1, round2)

        return game

    """
    " Metodo que monta os jogos dos playoffs com o resultado de cada jogo ida e volta
    """
    def mountGamePlayoffs(data, team1, team2, round1, round2):
        matches1 = data['rounds'][round1]['matches']

        # recupera os dados do primeiro round da fase
        match1_result = ChampionsLeagueModel.findTeamsInMatches(matches1, team1, team2)

        result = dict()
        # verifica se a resposta esta com erro (nao encontrada a partida 1)
        if 'Error' in match1_result:
            matches2 = data['rounds'][round2]['matches']
            # recupera os dados do segundo round da fase
            match2_result = ChampionsLeagueModel.findTeamsInMatches(matches2, team1, team2)

            # verifica se a resposta esta com erro (nao encontrada a partida 2)
            if 'Error' in match2_result:
                raise Exception('Match not found')
            # Encontrou no round 2
            else:
                result = match2_result
        # Encontrou no round 1
        else:
            result = match1_result

        # atribui os escores de cada time
        score1 = result['score1']
        score2 = result['score2']

        # cria a resposta para retorno do json com o jogo e o placar
        game = dict()
        game['Match'] = str(result['team1']['name']) + ' ' + str(score1) + ' vs ' + str(score2) + ' ' + str(
            result['team2']['name'])

        return game

    """
    " Metodo para procurar se os times informados nas partidas
    """
    def findTeamsInMatches(matches, t1, t2):

        match_found = dict()
        # cria um loop para verificar nas partidas se encontra a combinacao de times informados
        for m in range(0, len(matches)):

            # verifica se encontrou o time1
            if matches[m]['team1']['key'] == t1.lower():
                # verifica se encontrou o time1, caso encontre sai do loop
                if matches[m]['team2']['key'] == t2.lower():
                    match_found = matches[m]
                    break
                else:
                    # retorna informacao de não encontrado time 2
                    match_found = {'Error': 'Team2 ' + t2.lower() + ' Not found'}
                    break
            else:
                # retorna informacao de não encontrado time 1
                match_found = {'Error': 'Team1 ' + t1.lower() + ' Not found'}

        return match_found

    """
    " Metodo que recupera as informacoes da final
    """
    def getFinal(season, time1, time2):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        # recupera os dados do dataset
        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        # recupera somente a partida final
        matches = data['rounds'][12]['matches'][0]

        # verifica se o time 1 e time 2 informados estao corretos
        if matches['team1']['key'] != time1.lower():
            raise Exception('Invalid Team 1')
        if matches['team2']['key'] != time2.lower():
            raise Exception('Invalid Team 2')

        # atribui os escores de cada time
        score1 = matches['score1']
        score2 = matches['score2']

        # cria a resposta para retorno do json com o jogo e o placar
        game = dict()
        game['Match'] = str(matches['team1']['name']) + ' ' + str(score1) + " vs " + str(score2) + ' ' + str(
            matches['team2']['name'])

        # recupera os dados sobre a fina; da temporada
        finals = ChampionsLeagueModel.getAboutBySeason(season)
        # adiciona campeão e vice aos dados de retorno
        game['Champion'] = finals['champion']
        game['Runner-up'] = finals['runner-up']

        return game
