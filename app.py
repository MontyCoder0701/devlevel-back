from flask import Flask, request, jsonify
from model import new_soup, new_url
from views import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return {'status': 'server is running'}

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    username = data['username']

    repo_url = new_url(username, "repos")
    repo_soup = new_soup(repo_url)

    default_url = new_url(username, "default")
    default_soup = new_soup(default_url)

    languages = get_top_languages(repo_soup)
    contributions = get_contributions_count(default_soup)
    years_active = get_years_active(default_soup, username)

    response = {
        'languages': analyze_languages(languages),
        'contributions': analyze_contributions(contributions),
        'years_active': analyze_years_active(years_active)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)