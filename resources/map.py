from flask import render_template, Response
from flask_restful import Resource


class Map(Resource):
    @classmethod
    def get(cls):
        """Scikit-Learn Map"""
        return Response(render_template('map.html'))