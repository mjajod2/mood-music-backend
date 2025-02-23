from flask import Flask, request, jsonify, Blueprint
from .llm_calls import send_genre_request_to_llm, send_artist_recommendation_request_to_llm, send_request_for_language


moodToGenre = Blueprint('moodToGenre', __name__, url_prefix='/moodToGenre')

# endpoint to check health of api
@moodToGenre.route('/checkHealth', methods=['GET'])
def check_health():
    return jsonify({'success':True, 'msg': 'OK'}), 200

# endpoint to get genre suggestion based on user mood
@moodToGenre.route('/userMood', methods=['POST'])
def user_mood_request():
    try:
        data = request.get_json()
        mood_query = data['query']
        print(mood_query)
        genre_suggested = send_genre_request_to_llm(mood_query)
        print(f'genre_suggested: {genre_suggested}')
        return jsonify({'success':True, 'genre': genre_suggested}), 200
    except Exception as e:
        return jsonify({'success':False, 'msg': str(e)}), 500

# endpoint to get artist recommendation based on user query
@moodToGenre.route('/artistRecommendation', methods=['POST'])
def artist_recommendation_request():
    try:
        data = request.get_json()
        artist_query = data['query']
        print(artist_query)
        artist = send_artist_recommendation_request_to_llm(artist_query)
        print(f'artist: {artist}')
        return jsonify({'success':True, 'artist': artist}), 200
    except Exception as e:
        return jsonify({'success':False, 'msg': str(e)}), 500
    
@moodToGenre.route('/specificLanguage', methods=['POST'])
def recommend_language_songs():
    try:
        data = request.get_json()
        query = data['query']
        language = data['language']
        recommendation = send_request_for_language(query, language)
        print(f'recommendation: {recommendation}')
        return jsonify({'success':True, 'recommendation': recommendation}), 200
    except Exception as e:
        return jsonify({'success':False, 'msg': str(e)}), 500