import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    "home_team": "Ac Milan",
    "away_team": "atalanta bc"
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)
print(response.json())

"""
 output 
 {
    'away_team': 'atalanta bc',
    'home_team': 'Ac Milan',
    'predicted_away_goals': 3,
    'predicted_home_goals': 4
}

"""
