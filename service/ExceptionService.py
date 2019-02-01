__author__ = "João Paulo Leite Nascimento"
__date__ = "31 January 2019"
__email__ = "joaopauloln7@gmail.com"


import os.path

"""
" Service ExceptionService
"""


class ExceptionService:

    """
    " Metodo que gera exceção de temporada não encontrada
    """

    @staticmethod
    def raise_error_if_season_not_found(season):
        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

    """
    " Metodo que gera exceção de partida não encontrada
    """

    @staticmethod
    def raise_error_if_match_not_found():
        raise Exception('Match not found')

    """
    " Metodo que gera exceção do time nao encontrado
    """

    @staticmethod
    def raise_error_if_team_not_found(num, team):
        raise Exception('Invalid Team ' + str(num) + ' : ' + str(team))

    """
    " Metodo que verifica se os times da final estao corretos
    """

    @classmethod
    def raise_error_if_team_not_found_final(cls, matches, time1, time2):

        # verifica se o time 1 e time 2 informados estao corretos
        if matches['team1']['key'] != time1.lower():
            cls.raise_error_if_team_not_found(1, team=time1)
        if matches['team2']['key'] != time2.lower():
            cls.raise_error_if_team_not_found(2, team=time2)


