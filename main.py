from sanic import Sanic
from sanic.response import json, text
from service.ChampionsLeagueService import ChampionsLeagueService

__author__ = "João Paulo Leite Nascimento"
__date__ = "31 January 2019"
__email__ = "joaopauloln7@gmail.com"

app = Sanic('Champions League Challenge')

# api path variable
PATH_API = '/api'

"""
" Route home
"""


@app.route("/", methods=['GET'])
async def home(request):
    return text('API REST CHAMPIONS LEAGUE')

"""
" API home
"""


@app.route(PATH_API, methods=['GET'])
async def home(request):
    return text('API REST CHAMPIONS LEAGUE')

"""
" 1. Route about
"""


@app.route(PATH_API + "/champions-league/", methods=['GET'])
async def about(request):
    return json(ChampionsLeagueService.get_about())


"""
" 2. Route aboutFinal
"""


@app.route(PATH_API + "/champions-league/<season>", methods=['GET'])
async def about_final(request, season):
    try:
        ret = ChampionsLeagueService.get_about_by_season(season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 3. Route get all teams
"""


@app.route(PATH_API + "/champions-league/<season>/teams/", methods=['GET'])
async def teams(request, season):
    try:
        ret = ChampionsLeagueService.get_all_teams(season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 4. Route get one team
"""


@app.route(PATH_API + "/champions-league/<season>/teams/<name>", methods=['GET'])
async def team(request, season, name):
    try:
        ret = ChampionsLeagueService.get_one_team(season, name)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 5. Route get all groups
"""


@app.route(PATH_API + "/champions-league/<season>/group-stage/", methods=['GET'])
async def groups(request, season):
    try:
        ret = ChampionsLeagueService.get_groups(season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 6. Route get one group variable name using only one letter between A and H
"""


@app.route(PATH_API + "/champions-league/<season>/group-stage/<name>", methods=['GET'])
async def group(request, season, name):
    try:
        ret = ChampionsLeagueService.get_groups(season, name)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 7. Route round of 16
"""


@app.route(PATH_API + "/champions-league/<season>/round-of-16/", methods=['GET'])
async def round16(request, season):
    try:
        ret = ChampionsLeagueService.get_round_16(season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 8. Route round of 16 separated
"""


@app.route(PATH_API + "/champions-league/<season>/round-of-16/<team1>/vs/<team2>", methods=['GET'])
async def round_of_16_team_vs_team(request, season, team1, team2):
    try:
        ret = ChampionsLeagueService.get_playoffs(season, team1, team2, 'round-of-16')
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 9. Route quarter-finals
"""


@app.route(PATH_API + "/champions-league/<season>/quarter-finals/<team1>/vs/<team2>", methods=['GET'])
async def quarter_finals_team_vs_team(request, season, team1, team2):
    try:
        ret = ChampionsLeagueService.get_playoffs(season, team1, team2, 'quarter-finals')
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 10. Route semi-finals
"""


@app.route(PATH_API + "/champions-league/<season>/semi-finals/<team1>/vs/<team2>", methods=['GET'])
async def semi_finals_team_vs_team(request, season, team1, team2):
    try:
        ret = ChampionsLeagueService.get_playoffs(season, team1, team2, 'semi-finals')
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


"""
" 11 Route Final
"""


@app.route(PATH_API + "/champions-league/<season>/final/<team1>/vs/<team2>", methods=['GET'])
async def final(request, season, team1, team2):
    try:
        ret = ChampionsLeagueService.get_final(season, team1, team2)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
