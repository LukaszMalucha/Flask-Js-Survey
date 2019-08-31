from flask import request, Response, render_template
from flask_restful import Resource
from libs.strings import gettext
from models.algorithm import AlgorithmCollection


class Algorithms(Resource):

    @classmethod
    def get(cls):
        suggested_algorithms = AlgorithmCollection.find_all()
        return Response(render_template('algorithms.html', suggested_algorithms=suggested_algorithms))

    @classmethod
    def post(cls):

        algorithm_json = request.get_json()

        if AlgorithmCollection.find_by_name(algorithm_json['name']):
            return {"message": gettext("algorithm_name_exists").format(algorithm_json['name']), 'status': 400}

        try:
            mongodb = AlgorithmCollection()
            mongodb.insert_algorithm(algorithm_json)
        except:
            return {"message": gettext("algorithm_error_inserting"), 'status': 500}

        return {'message': gettext("algorithm_uploaded").format(algorithm_json['name']),
                'name': algorithm_json['name'],
                'description': algorithm_json['description'],
                'status': 200}

    @classmethod
    def delete(cls):
        algorithm_json = request.get_json()
        if not AlgorithmCollection.find_by_name(algorithm_json['name']):
            return {"message": gettext("algorithm_not_found").format(algorithm_json['name']), 'status': 400}
        try:
            mongodb = AlgorithmCollection()
            mongodb.delete_algorithm(algorithm_json['name'])
        except:
            return {"message": gettext("algorithm_error_deleting"), 'status': 500}

        return {"message": gettext("algorithm_deleted"), 'status': 200}
