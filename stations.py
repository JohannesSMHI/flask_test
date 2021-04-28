"""
Created on 2021-03-25 20:45
@author: johannes
"""
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
from shp_handler import ShapeHandler

app = Flask(__name__)
api = Api(app)


class Stations(Resource):
    def __init__(self):
        super().__init__()
        self.sh = ShapeHandler()

    def get(self):
        # example data
        return self.sh.get_example(), 200  # return data and 200 OK

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('lat', required=True)
        parser.add_argument('lon', required=True)
        parser.add_argument('key', required=False)
        args = parser.parse_args()  # parse arguments to dictionary

        if args['lat'] and args['lon'] and not args['key']:
            return self.sh.find_area_for_point(
                args['lat'],
                args['lon']
            ), 200
        elif args['lat'] and args['lon'] and args['key']:
            return self.sh.get_key_value_for_point(
                args['lat'],
                args['lon'],
                args['key']
            ), 200
        else:
            return {
                       'message': f"'{args['userId']}' already exists."
                   }, 409


api.add_resource(Stations, '/stations')


if __name__ == '__main__':
    app.run()  # run our Flask app
