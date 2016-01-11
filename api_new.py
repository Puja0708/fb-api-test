from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:////home/puja/Documents/fb-api-test/fb-api.db')

app = Flask(__name__)
api = Api(app)



class fb_api(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from fb_api_test ORDER BY author")
        result = {'data': [dict(zip(tuple (query.keys()) ,i) )for i in query.cursor]}
        return result
 
api.add_resource(fb_api, '/fb-api')
# api.add_resource(Departments_Meta, '/departments')

if __name__ == '__main__':
    app.run()