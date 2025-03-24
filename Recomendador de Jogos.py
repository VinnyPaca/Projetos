from flask import Flask, request, jsonify
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)


games = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'title': ['The Witcher 3', 'Cyberpunk 2077', 'Dark Souls 3', 'DOOM Eternal', 'Red Dead Redemption 2'],
    'genre': ['RPG, Action', 'RPG, FPS, Open World', 'RPG, Soulslike', 'FPS, Action', 'Action, Open World']
})

vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(games['genre'])


def recommend_games(game_title, top_n=3):
    if game_title not in games['title'].values:
        return []

    game_index = games[games['title'] == game_title].index[0]
    similarities = cosine_similarity(genre_matrix[game_index], genre_matrix).flatten()
    recommended_indices = similarities.argsort()[-(top_n + 1):-1][::-1]  # Exclui o próprio jogo e ordena

    return games.iloc[recommended_indices][['title', 'genre']].to_dict(orient='records')


@app.route('/')
def home():
    return "<h1>Bem-vindo ao Recomendador de Jogos! Use /recommend?game=Jogo para recomendações.</h1>"


@app.route('/recommend', methods=['GET'])
def recommend():
    game_title = request.args.get('game')
    if not game_title:
        return jsonify({'error': 'Please provide a game title'}), 400

    recommendations = recommend_games(game_title)
    if not recommendations:
        return jsonify({'error': 'Game not found in the database'}), 404

    return jsonify({'recommendations': recommendations})


if __name__ == '__main__':
    app.run(debug=True)
