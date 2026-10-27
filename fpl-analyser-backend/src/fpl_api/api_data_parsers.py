from api_getters import get_bootstrap_static

# TODO: Change this to check bootstrap first.
element_type_id_to_name = {
    1: "GKP",
    2: "DEF",
    3: "MID",
    4: "FWD"
}


def get_teams(data: dict[str, any]):
    """Expects dictionary in the form of a bootstrap-static response and returns list of teams for the given season and their details."""
    teams = [
        {
            "fpl_team_code": team["code"],
            "season_fpl_team_id": team["id"],
            "team_name": team["name"],
            "short_name": team["short_name"]
        } for team in data["teams"]
    ]
    return teams


def get_players(data: dict[str, any]):
    """Expects dictionary in the form of a bootstrap-static response and returns list of players for the given season and their details."""
    players = [
        {
            "fpl_player_code": player["code"],
            "season_fpl_player_id": player["id"],
            "first_name": player["first_name"],
            "second_name": player["second_name"],
            "fpl_position": element_type_id_to_name[player["element_type"]],
            "season_fpl_team_id": player["team"],
            # "fpl_team_code": player["team_code"],
            "team_join_date": player["team_join_date"]
        } for player in data["elements"]
    ]
    return players

if __name__ == "__main__":
    data = get_bootstrap_static()
    print(get_players(data))