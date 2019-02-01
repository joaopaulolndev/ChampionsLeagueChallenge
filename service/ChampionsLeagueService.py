__author__ = "João Paulo Leite Nascimento"
__date__ = "31 January 2019"
__email__ = "joaopauloln7@gmail.com"

import os.path
from model.ChampionsLeagueModel import ChampionsLeagueModel
from service.ExceptionService import ExceptionService

"""
" Service ChampionsLeagueService
"""


class ChampionsLeagueService:
    """
    " Metodo com descricao sobre a liga dos campeões, maiores vencedores e maiores artilheiros
    """

    @classmethod
    def get_about(cls):

        # recupera os dados da model
        return ChampionsLeagueModel.get_champions_league_json()

    """
    " Metodo retorno o pais que recebeu a final, o time campeão e o vice
    """

    @classmethod
    def get_about_by_season(cls, season):

        # recupera os dados da model
        data = ChampionsLeagueModel.get_finals_json()

        # verifica se tem a final informada
        if season is not data['finals']:
            ExceptionService.raise_error_if_season_not_found(season)

        return data['finals'][season]

    """
    " Metodo que recupera todos os times da temporada com as suas informacoes
    """

    @classmethod
    def get_all_teams(cls, season):

        # valida se a temporada informada existe
        ExceptionService.raise_error_if_season_not_found(season)

        # recupera os dados da model
        return ChampionsLeagueModel.get_clubs_json(season)

    """
    " Metodo que recupera somente um pais com a quantidade de titulos, país de origem
    """

    @classmethod
    def get_one_team(cls, season, name):

        # valida se a temporada informada existe
        ExceptionService.raise_error_if_season_not_found(season)

        # recupera os dados da model
        data = ChampionsLeagueModel.get_clubs_json(season)

        # executa o filter com lambda somente para recuperar o nó que está o time pesquisado
        output = list(filter(lambda x: x['key'].lower() == name.lower(), data['clubs']))

        # verifica se retornou em vazio
        if not output:
            ExceptionService.raise_error_if_team_not_found(1, name)

        return output[0]

    """
    " Metodo que recupera todos os grupos da temporada
    """

    @classmethod
    def get_groups(cls, season, group=None):

        # valida se a temporada informada existe
        ExceptionService.raise_error_if_season_not_found(season)

        # recupera os dados da model
        data = ChampionsLeagueModel.get_groups_json(season)

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

    @classmethod
    def get_round_16(cls, season):

        # valida se a temporada informada existe
        ExceptionService.raise_error_if_season_not_found(season)

        # recupera os dados da model
        data = ChampionsLeagueModel.get_cl_json(season)

        # recupera somente os jogos das oitavas de final
        matches = data['rounds'][6]['matches']

        # faz um loop para montar o chaveamento das oitavas de final
        games = dict()
        for i in range(0, len(matches)):
            games['Match ' + str(i + 1)] = str(matches[i]['team1']['name']) + " vs " + str(matches[i]['team2']['name'])

        return games

    """
    " Metodo para criação dos playoffs das oitavas de final as semi finais
    """

    @classmethod
    def get_playoffs(cls, season, team1, team2, step):

        # valida se a temporada informada existe
        ExceptionService.raise_error_if_season_not_found(season)

        # recupera os dados da model
        data = ChampionsLeagueModel.get_cl_json(season)

        # verifica qual é a fase ao qual está sendo feita a consulta para recuperar os rounds
        if step == 'round-of-16':
            round1, round2 = 6, 7
        elif step == 'quarter-finals':
            round1, round2 = 8, 9
        elif step == 'semi-finals':
            round1, round2 = 10, 11

        # faz chamada ao metodo que monta as partidas
        game = cls.mount_game_playoffs(data, team1, team2, round1, round2)

        return game

    """
    " Metodo que monta os jogos dos playoffs com o resultado de cada jogo ida e volta
    """

    @classmethod
    def mount_game_playoffs(cls, data, team1, team2, round1, round2 = ''):

        matches1 = data['rounds'][round1]['matches']

        # recupera os dados do primeiro round da fase
        match1_result = cls.find_teams_in_matches(matches1, team1, team2)

        result = dict()
        # verifica se a resposta esta com erro (nao encontrada a partida 1)
        if 'Error' in match1_result:
            matches2 = data['rounds'][round2]['matches']
            # recupera os dados do segundo round da fase
            match2_result = cls.find_teams_in_matches(matches2, team1, team2)

            # verifica se a resposta esta com erro (nao encontrada a partida 2)
            if 'Error' in match2_result:
                ExceptionService.raise_error_if_match_not_found()
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
        game['Date'] = result['date']
        game['Match'] = str(result['team1']['name']) + ' ' + str(score1) + ' vs ' + str(score2) + ' ' + str(
            result['team2']['name'])

        # verifica se houve gols na partida
        if 'goals1' in result or 'goals2' in result:
            game['Goals'] = cls.goals_of_match(result)

        return game

    """
    " Metodo para procurar se os times informados nas partidas
    """

    @staticmethod
    def find_teams_in_matches(matches, t1, t2):

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
                    match_found = {'Error': 'Team 2 ' + t2.lower() + ' Not found'}
                    break
            else:
                # retorna informacao de não encontrado time 1
                match_found = {'Error': 'Team 1 ' + t1.lower() + ' Not found'}

        return match_found

    """
    " Metodo que recupera as informacoes da final
    """

    @classmethod
    def get_final(cls, season, time1, time2):

        # valida se a temporada informada existe
        ExceptionService.raise_error_if_season_not_found(season)

        # recupera os dados da model
        data = ChampionsLeagueModel.get_cl_json(season)

        # recupera somente a partida final
        matches = data['rounds'][12]['matches'][0]

        # recupera a validacao dos times
        ExceptionService.raise_error_if_team_not_found_final(matches, time1, time2)

        # recupera o resultado do jogo final
        game = cls.mount_game_playoffs(data, time1, time2, round1=12)

        # recupera os dados sobre a fina; da temporada
        finals = cls.get_about_by_season(season)

        # adiciona campeão e vice aos dados de retorno
        game['Champion'] = finals['champion']
        game['Runner-up'] = finals['runner-up']

        return game

    @staticmethod
    def goals_of_match(result):

        goals = dict()
        goals[result['team1']['name']] = ''
        for g in result['goals1']:
            goals[result['team1']['name']] += g['name'] + '(' + str(g['minute']) + 'min), '

        goals[result['team2']['name']] = ''
        for g in result['goals2']:
            goals[result['team2']['name']] += g['name'] + '(' + str(g['minute']) + 'min), '

        return goals

