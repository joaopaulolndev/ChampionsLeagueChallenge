__author__ = "João Paulo Leite Nascimento"
__date__ = "31 January 2019"
__email__ = "joaopauloln7@gmail.com"

import json

"""
" model ChampionsLeagueModel
"""


class ChampionsLeagueModel:
    """
    " Metodo que gera recupera os dados json champions-league
    """

    @classmethod
    def get_champions_league_json(cls):
        # recupera os dados do dataset e retorna
        return cls.read_json_file('champions-league.json')

    """
    " Metodo que gera recupera os dados json finals
    """

    @classmethod
    def get_finals_json(cls):
        # recupera os dados do dataset e retorna
        return cls.read_json_file('finals.json')

    """
    " Metodo que gera recupera os dados clubs
    """

    @classmethod
    def get_clubs_json(cls, season):
        # recupera os dados do dataset e retorna
        return cls.read_json_file(season + '/cl.clubs.json')

    """
    " Metodo que gera recupera os dados groups
    """

    @classmethod
    def get_groups_json(cls, season):
        # recupera os dados do dataset e retorna
        return cls.read_json_file(season + '/cl.groups.json')

    """
    " Metodo que gera recupera os dados cl
    """

    @classmethod
    def get_cl_json(cls, season):
        # recupera os dados do dataset e retorna
        return cls.read_json_file(season + '/cl.json')

    """
    " Metodo que recupera os dados json
    """

    @staticmethod
    def read_json_file(file):
        json_data = open('data/' + file).read()
        return json.loads(json_data)
