import os
from flask import g
from flask_oauthlib.client import OAuth

oauth = OAuth()

github = oauth.remote_app(
    'github',
    consumer_key=os.environ.get("GITHUB_CONSUMER_KEY"),  # consumer token
    consumer_secret=os.environ.get("GITHUB_CONSUMER_SECRET"),  # secret token
    request_token_params={"scope": "user:email"},  # add to request, what we want to get back
    base_url="https://api.github.com/",  # service url
    request_token_url=None,  # None for OAuth 2.0
    access_token_method="POST",
    access_token_url="https://github.com/login/oauth/access_token", # where we send data to get access token (from docs)
    authorize_url="https://github.com/login/oauth/authorize"  # where we send user in initial request (from github docs)
)
# http://localhost:5000/login/github/authorized
@github.tokengetter
def get_github_token():
    if 'access_token' in g:
        return g.access_token