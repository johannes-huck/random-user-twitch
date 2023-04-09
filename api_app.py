from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests
import random
import ast

app = Flask(__name__)
api = Api(app)

class RandomUser(Resource):
     def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('channelID', required=True, location='args')  # add args
        parser.add_argument('moderatorID', required=True, location='args')
        parser.add_argument('token', required=True, location='args')
        args = parser.parse_args()  # parse arguments to dictionary
        channelID = args['channelID']
        moderatorID = args['moderatorID']
        token = args['token']
        url = f'https://api.twitch.tv/helix/chat/chatters?broadcaster_id={channelID}&moderator_id={moderatorID}'
        headers = {'Authorization': f'Bearer {token}', 'Client-Id': 'o5srkuosq373r07gzbckz7xj6hkj1i'}
        r = requests.get(url, headers=headers)
        json_data = r.json()
        rd = random.randint(0, len(json_data['data'])-1)
        return json_data['data'][rd]['user_name']

    
    
api.add_resource(RandomUser, '/randomuser')  # '/randomuser' is our entry point for Users

if __name__ == '__main__':
    app.run()  # run our Flask app