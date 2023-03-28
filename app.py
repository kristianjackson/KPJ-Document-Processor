from flask import Flask, redirect, request, session, url_for
from flask_dance.contrib.github import make_github_blueprint, github

# Replace these values with your own GitHub OAuth settings
CLIENT_ID = 'your-github-client-id'
CLIENT_SECRET = 'your-github-client-secret'

app = Flask(__name__)
app.secret_key = 'your-secret-key'
blueprint = make_github_blueprint(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    if not github.authorized:
        return redirect(url_for('github.login'))
    resp = github.get('/user')
    assert resp.ok
    return 'You are {name} on GitHub'.format(name=resp.json()['login'])

if __name__ == '__main__':
    app.run()
