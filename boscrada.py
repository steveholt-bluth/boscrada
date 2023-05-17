# Example script using requests and json
import requests
import json

# Get the JSON data from the API
url = "https://www.bovada.lv/services/sports/event/v2/events/A/description/hockey/nhl"
response = requests.get(url)
data = response.json()

# Loop through all the games
for game in data[0]["events"]:
    # Get the team names from the competitors section
    teams = [team["name"] for team in game["competitors"]]
    # Get the odds from the displayGroups section
    odds = []
    for market in game["displayGroups"][0]["markets"]:
        # Check if the market is Moneyline
        if market["description"] == "Moneyline":
            # Get the prices for each outcome
            for outcome in market["outcomes"]:
                odds.append(outcome["price"]["american"])
    # Print the team names and odds
    print(f"{teams[0]} vs {teams[1]}: {odds[0]} / {odds[1]}")
