__author__ = "João Paulo Leite Nascimento"
__date__ = "31 January 2019"
__email__ = "joaopauloln7@gmail.com"

import json
import os.path


# Model ChampionsLeagueModel
class ChampionsLeagueModel:

    # about: description, top 5 champions, top 5 scorer,
    def getAbout():

        json_data = open('data/champions-league.json').read()
        data = json.loads(json_data)
        return data

    # country receive the final, champion and vice
    def getAboutBySeason(season):

        json_data = open('data/finals.json').read()
        data = json.loads(json_data)

        if (season in data['finals']):
            ret = data['finals'][season]
        else:
            raise Exception('Season not found')

        return ret

    # get all teams in the season
    def getAllTeams(season):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        json_data = open('data/' + season + '/cl.clubs.json').read()
        return json.loads(json_data)

    # get one team
    def getOneTeam(season, name):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        json_data = open('data/' + season + '/cl.clubs.json').read()
        data = json.loads(json_data)

        output = list(filter(lambda x: x['key'].lower() == name.lower(), data['clubs']))

        return output[0]

    # get groups
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

    # get round of 16 list
    def getRound16(season):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        matches = data['rounds'][6]['matches']

        games = dict()
        for i in range(0, len(matches)):
            games['Match ' + str(i+1)] = str(matches[i]['team1']['name']) + " vs " + str(matches[i]['team2']['name'])

        return games

    # get final
    def getFinal(season, time1, time2):

        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')

        json_data = open('data/' + season + '/cl.json').read()
        data = json.loads(json_data)

        qtdRound = ( 18 if season == '2015-16' else 12)

        matches = data['rounds'][qtdRound]['matches'][0]

        if matches['team1']['key'] != time1.lower():
             raise Exception('Invalid Team 1')
        if matches['team2']['key'] != time2.lower():
            raise Exception('Invalid Team 2')

        score1 = matches['score1']
        score2 = matches['score2']

        game = dict()
        game['Match'] = str(matches['team1']['name'])+' '+str(score1)+" vs "+str(score2)+' '+str(matches['team2']['name'])

        finals = ChampionsLeagueModel.getAboutBySeason(season)

        game['Champion'] = finals['champion']
        game['Runner-up'] = finals['runner-up']

        return game
