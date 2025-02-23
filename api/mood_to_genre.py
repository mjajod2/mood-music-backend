from flask import Flask, request, jsonify, Blueprint

moodToGenre = Blueprint('moodToGenre', __name__, url_prefix='/moodToGenre')

# endpoint to check health of api
@moodToGenre.route('/checkHealth', methods=['GET'])
def check_health():
    return jsonify({'success':True, 'msg': 'OK'}), 200