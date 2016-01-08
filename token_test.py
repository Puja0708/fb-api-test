import facebook
from flask_oauth import OAuth
from flask import Flask

oauth = OAuth()
facebook_id = '727256290662770'
page_id = '116151972998'
# test = oauth(page_id)
# print test
app = Flask(__name__)
app.debug = True
oauth_access_token = 'CAACEdEose0cBABv8jDRTbhZCVubsWqY2NZBYMn9RInnS0JPaQRMe38tpZCd78GUOutmHwdtHQEOSmIUmsrcCY9oMVZAlrKcZCDZBSiphXW3jdHK9KRuMjkxD5ZAWrS2nSYjDthcdLUqdSy3hFwtq1LPsJEV28zgtqiB58wsPiBwWKbCjsKEPHQNt2o6rGrEDpZAGKcvAAih6TAZDZD'
graph = facebook.GraphAPI(oauth_access_token)
profile = graph.get_object("me")
print profile

graph_url = 'https://graph.facebook.com/'
facebook = oauth.remote_app(name='facebook',
                         authorize_url='https://www.facebook.com/dialog/oauth',
                         access_token_url=graph_url + 'oauth/access_token',
                         client_id=app.config['116151972998'],
                         base_url=graph_url)
print facebook

if __name__ == '__main__':
    app.run()