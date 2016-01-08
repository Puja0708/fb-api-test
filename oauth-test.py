from rauth import OAuth2Service

app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '470154729788964',
        'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'
    }
}

class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
            name='facebook',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://graph.facebook.com/oauth/authorize',           
            access_token_url='https://graph.facebook.com/oauth/access_token',
            base_url='https://graph.facebook.com/'
        )