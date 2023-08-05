from flask import Flask, request, jsonify
from model import new_soup, new_url
from views import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return {'status': 'server is running'}

@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.get_json()
        username = data['username']

        if username == "" or username == None:
            return jsonify({'error': 'username is empty'})

    except KeyError as e:
        return jsonify({'error': f'{e} is missing'})

    repo_url = new_url(username, "repos")
    repo_soup = new_soup(repo_url)

    default_url = new_url(username, "default")
    default_soup = new_soup(default_url)

    languages = get_top_languages(repo_soup)

    try:
        contributions = get_contributions_count(default_soup)
    except AttributeError:
        return jsonify({'error': 'user does not exist'}), 400
    
    years_active = get_years_active(default_soup)

    response = {
        'stack': analyze_stack(languages),
        'languages': analyze_languages(languages),
        'contributions': analyze_contributions(contributions),
        'expertise' : analyze_expertise(years_active),
        'years_active': analyze_years_active(years_active)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
