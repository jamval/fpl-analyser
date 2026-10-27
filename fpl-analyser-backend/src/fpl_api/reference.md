# FPL API Reference

## Bootstrap Static

URL: https://fantasy.premierleague.com/api/bootstrap-static/

Returns JSON object containing: chips, events, game_settings, phases, teams, total_players, element_stats, element_types, elements, 

### Chips

### Events
List of the gameweeks for the current season.

Important fields:
 - 'id': same as gameweek number (1 for gw1, 12 for gw12, etc...).
 - 'name': name of the gameweek (e.g. gw1 is "Gameweek 1").
 - 'deadline_time': in format yyyy-mm-ddThh:mm:ssZ (e.g. gw1 was 2026-08-21T17:30:00Z).
 - 'average_entry_score': average score of all managers in the gameweek.
 - 'finished': boolean value, true if the gameweek has finished.
 - 'is_previous': boolean value, true if the gameweek is the previous gameweek.
 - 'is_current': boolean value, true if the gameweek is the current gameweek.
 - 'is_next': boolean value, true if the gameweek is the next gameweek.

Also contains details of highest scores, how many of each chip were played, who was most transferred in, etc.

### Game Settings

### Phases

### Teams
List of teams in alphabetical order.

Important fields:
 - 'id': team id.
 - 'name': team name.
 - 'short_name': short name of the team (e.g. ARS for Arsenal).
 - 'code': Unsure? Possibly id that remains the same each season?

### Total Players
Single value of total number of players (managers).

### Element Stats
List of all stats that are recorded for each element (player).

### Element Types
List of all types of elements (goalkeeper, defender, midfielder, forward).

Important fields:

| Position   | 'id' | 'plural_name' | 'plural_name_short' | 'singular_name' | 'singular_name_short' |
|------------|------|---------------|---------------------|-----------------|-----------------------|
| Goalkeeper | 1    | Goalkeepers   | GKP                 | Goalkeeper      | GKP                   |
| Defender   | 2    | Defenders     | DEF                 | Defender        | DEF                   |
| Midfielder | 3    | Midfielders   | MID                 | Midfielder      | MID                   |
| Forward    | 4    | Forwards      | FWD                 | Forward         | FWD                   |

Also contains details of max/min number of each type can be played in a team, and 'element_count' (number of elements of each type).

### Elements
List of all elements (players that can be added to a team) and information about them.

Important fields:
 - 'id': element id.
 - 'code': Unique id that doesn't change each season (regular id does change each season).
 - 'opta_code'
 - 'element_type': player's position (e.g. goalkeeper, defender, etc...).
 - 'first_name': player's first name.
 - 'second_name': player's second name(s).
 - 'team': id of the team that the player plays for.
 - 'event_points': points scored in the current gameweek.
 - 'total_points': total points scored by the player.
 - 'now_cost': current price of the player without the decimal (e.g. 60 for £6.0m or 49 for £4.9m).
 - 'selected_by_percent': percentage of managers that have selected the player.
 - 'penalties_order': order of penalties (1 for first, 2 for second, 3 for third, null if not in contest).
 - 'corners_and_indirect_freekicks_order'
 - 'direct_freekicks_order'
 - 'chance_of_playing_next_round': chance of the player playing in the next gameweek (e.g. "75" if injured, null if no news that would stop the player from playing).
 - 'chance_of_playing_this_round'
 - 'photo': just the name of the file with no URL.
 - 'squad_number': Shirt number? says null for some.
 - 'team_join_date'

Also contains various stats such as 'minutes', 'goals_scored', 'assists', 'yellow_cards', 'tackles', defensive_contributions', etc...

Also contains details of projected price changes for each player.

## Live Gameweek

URL: https://fantasy.premierleague.com/api/event/{{gw_id}}/live/
 - E.g. https://fantasy.premierleague.com/api/event/1/live/

Returns JSON object containing list of elements (players) and information about each player for the relevant gameweek.

Each player has an 'id' field and a 'stats' field. The 'id' field represents the player's ID.

The 'stats' contains the following stats about each player.
 - 'minutes'
 - 'goals_scored'
 - 'assists'
 - 'clean_sheets'
 - 'goals_conceded'
 - 'own_goals'
 - 'penalties_saved'
 - 'penalties_missed'
 - 'yellow_cards'
 - 'red_cards'
 - 'saves'
 - 'bonus' - how many bonus points the player received.
 - 'bps' - metric for determining which player received bonus points in the week.
 - 'influence'
 - ' creativity'
 - 'threat'
 - 'ict_index'
 - 'clearances_blocks_interceptions'
 - 'recoveries'
 - 'tackles'
 - 'defensive_contributions'
 - 'starts'
 - 'expected_goals'
 - 'expected_assists'
 - 'expected_goal_involvements'
 - 'expected_goals_conceded' - check
 - 'total_points'
 - 'in_dreamteam'
 - 'played' - true or false depending on whether the player played in this gw.

## Entry's Live Gameweek Team

URL: https://fantasy.premierleague.com/api/my-team/{{team_id}}/

Returns an entry's (manager's) current team and other stats.

TODO

## Entry Details

URL: https://fantasy.premierleague.com/api/me/

TODO

## Entry Summary

URL: https://fantasy.premierleague.com/api/entry/{{team_id}}/

TODO

## Entry History

URL: https://fantasy.premierleague.com/api/entry/{{team_id}}/history/

TODO

## Entry Transfers

URL: https://fantasy.premierleague.com/api/entry/{{team_id}}/transfers/

TODO

## Gameweek Picks

TODO

## Gameweek Fixtures

URL: https://fantasy.premierleague.com/api/fixtures/
 - Get fixtures for a specific gameweek: https://fantasy.premierleague.com/api/fixtures/?event={{gw_id}}

Returns list of fixtures for the gw.

Each fixture object contains the following information:
 - 'code': fixture identifier that's unique across all recorded fixtures.
 - 'id': fixture identifier that's unique only to this season.
 - 'event': gameweek number.
 - 'finished': true or false
 - 'kickoff_time': in format yyyy-mm-ddThh:mm:ssZ (e.g., 2026-08-21T17:30:00Z).
 - 'minutes'
 - 'started': true or false.
 - 'team_a': id of the away team.
 - 'team_h': id of the home team.
 - 'team_a_score': final score of the away team (null if game hasn't started yet).
 - 'team_h_score': final score of the home team

Also contains 'stats' of which players did certain things (e.g., who scored etc...), if the match has finished. These stats can be found in live gameweek endpoint.

## Element Summary

URL:https://fantasy.premierleague.com/api/element-summary/{{player_id}}/
 - e.g., https://fantasy.premierleague.com/api/element-summary/1/

Returns a player's upcoming fixtures, a history of completed gws, and a summary from previous seasons.

TODO

## Event Status
