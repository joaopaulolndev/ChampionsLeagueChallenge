__author__ = "João Paulo Leite Nascimento"
__date__ = "31 January 2019"
__email__ = "joaopauloln7@gmail.com"

import json
import os.path


"""
" Model ChampionsLeagueModel
"""
class ChampionsLeagueModel:

    """
    " Metodo com descricao sobre a liga dos campeões, maiores vencedores e maiores artilheiros
    """
    def getAbout():

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

        json_data = open('data/' + season + '/cl.clubs.json').read()
        return json.loads(json_data)

    """
    " Metodo que recupera somente um pais com a quantidade de titulos, país de origem
    """
    def getOneTeam(season, name):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        json_data = open('data/' + season + '/cl.clubs.json').read()
        data = json.loads(json_data)

        output = list(filter(lambda x: x['key'].lower() == name.lower(), data['clubs']))

        return output[0]

    """
    " Metodo que recupera todos os grupos da temporada
    """
    def getGroups(season, group=None):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        json_data = open('data/' + season + '/cl.groups.json').read()
        data = json.loads(json_data)

        result = dict()
        for i in range(0, 8):
            result[data['groups'][i]['name']] = sorted(data['groups'][i]['teams'], key=lambda x: x['position'])

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

        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        matches = data['rounds'][6]['matches']

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

        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        if step == 'round-of-16':
            round1, round2 = 6, 7
        elif step == 'quarter-finals':
            round1, round2 = 8, 9
        elif step == 'semi-finals':
            round1, round2 = 10, 11

        game = ChampionsLeagueModel.mountGamePlayoffs(data, team1, team2, round1, round2)

        return game

    """
    " Metodo que monta os jogos dos playoffs com o resultado de cada jogo ida e volta
    """
    def mountGamePlayoffs(data, team1, team2, round1, round2):
        matches1 = data['rounds'][round1]['matches']

        match1_result = ChampionsLeagueModel.findTeamsInMatches(matches1, team1, team2)

        result = dict()
        if 'Error' in match1_result:
            matches2 = data['rounds'][round2]['matches']
            match2_result = ChampionsLeagueModel.findTeamsInMatches(matches2, team1, team2)

            if 'Error' in match2_result:
                raise Exception('Match not found')
            # Encontrou no 2
            else:
                result = match2_result
        # Encontrou no 1
        else:
            result = match1_result

        score1 = result['score1']
        score2 = result['score2']

        game = dict()
        game['Match'] = str(result['team1']['name']) + ' ' + str(score1) + ' vs ' + str(score2) + ' ' + str(
            result['team2']['name'])

        return game

    """
    " Metodo para procurar se os times informados nas partidas
    """
    def findTeamsInMatches(matches, t1, t2):

        match_found = dict()
        for m in range(0, len(matches)):

            if matches[m]['team1']['key'] == t1.lower():
                if matches[m]['team2']['key'] == t2.lower():
                    match_found = matches[m]
                    break
                else:
                    match_found = {'Error': 'Team2 ' + t2.lower() + ' Not found'}
                    break
            else:
                match_found = {'Error': 'Team1 ' + t1.lower() + ' Not found'}

        return match_found

    """
    " Metodo que recupera as informacoes da final
    """
    def getFinal(season, time1, time2):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        # Verifica o numero de rodadas ate a final
        qtdRound = (18 if season == '2015-16' else 12)

        matches = data['rounds'][qtdRound]['matches'][0]

        if matches['team1']['key'] != time1.lower():
            raise Exception('Invalid Team 1')
        if matches['team2']['key'] != time2.lower():
            raise Exception('Invalid Team 2')

        score1 = matches['score1']
        score2 = matches['score2']

        game = dict()
        game['Match'] = str(matches['team1']['name']) + ' ' + str(score1) + " vs " + str(score2) + ' ' + str(
            matches['team2']['name'])

        finals = ChampionsLeagueModel.getAboutBySeason(season)

        game['Champion'] = finals['champion']
        game['Runner-up'] = finals['runner-up']

        return game
