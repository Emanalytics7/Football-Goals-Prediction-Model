from flask import Flask, request, jsonify
import pandas as pd
from unidecode import unidecode
import joblib
import os

app = Flask(__name__)

current_dir = os.path.dirname(__file__)

model_path = os.path.join(current_dir, 'football_goals_prediction_model.pkl')
model = joblib.load(model_path)

csv_path = os.path.join(current_dir, 'team_avg_ratings.csv')
team_ratings = pd.read_csv(csv_path)

def get_team_rating(team_name, role="home"):
    if role == "home":
        rating_column = 'avg_rating_home'
    else:
        rating_column = 'avg_rating_away'

    normalized_name = unidecode(team_name).strip().lower()
    if normalized_name in team_ratings['team_name'].str.lower().values:
        return team_ratings.loc[team_ratings['team_name'].str.lower() == normalized_name, rating_column].values[0]
    else:
        return team_ratings[rating_column].mean()  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    home_team = data.get('home_team')
    away_team = data.get('away_team')
    
    home_team_rating = get_team_rating(home_team, "home")
    away_team_rating = get_team_rating(away_team, "away")
    
    input_data = pd.DataFrame({
        'home_team_avg_rating': [home_team_rating],
        'away_team_avg_rating': [away_team_rating]
    })
    
    goals_pred = model.predict(input_data)
    
    response = {
        'home_team': home_team,
        'away_team': away_team,
        'predicted_home_goals': int(goals_pred[0][0]),
        'predicted_away_goals': int(goals_pred[0][1])
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
