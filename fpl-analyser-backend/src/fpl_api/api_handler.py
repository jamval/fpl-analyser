import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import json


BASE_URL = "https://fantasy.premierleague.com/api/"
BOOTSTRAP_STATIC_URL = BASE_URL + "bootstrap-static/"
FIXTURES_URL = BASE_URL + "fixtures/"
EVENT_PARAM_KEY = "event"
GW_ID_PLACEHOLDER = "{{gw_id}}"
LIVE_GAMEWEEK_URL = BASE_URL + f"event/{GW_ID_PLACEHOLDER}/live/"
PLAYER_ID_PLACEHOLDER = "{{player_id}}"
ELEMENT_SUMMARY_URL = BASE_URL + f"element-summary/{PLAYER_ID_PLACEHOLDER}/"


def make_request(url: str, params: dict[str, str] | None = None):
    try:
        response = requests.get(url, timeout=5, params=params)
        response.raise_for_status()
        return json.loads(response.text)
    except HTTPError:
        print(f"Request failed with status code: {response.status_code}.")
    except Timeout:
        print("The request timed out.")
    except RequestException as e:
        print(f"An unexpected network error occurred: {e}")


def get_bootstrap_static():
    return make_request("https://fantasy.premierleague.com/api/bootstrap-static/")


def get_fixtures(gw_id: int | None = None):
    params = {EVENT_PARAM_KEY: str(gw_id)} if gw_id else None
    return make_request(FIXTURES_URL, params)


def get_live_gameweek(gw_id: int):
    return make_request(LIVE_GAMEWEEK_URL.replace(GW_ID_PLACEHOLDER, str(gw_id)))


def get_player_summary(player_id: int):
    return make_request(ELEMENT_SUMMARY_URL.replace(PLAYER_ID_PLACEHOLDER, str(player_id)))


if __name__ == "__main__":
    data = get_bootstrap_static()
    with open("bootstrap.json", "w") as out:
        json.dump(data, out, indent=4)