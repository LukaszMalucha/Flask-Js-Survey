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

        if AlgorithmCollection.find_by_name(algorithm_json['algorithm']):
            return {"message": gettext("algorithm_name_exists").format(algorithm_json['algorithm']), 'status': 400}

        try:
            mongodb = AlgorithmCollection()
            mongodb.insert_algorithm(algorithm_json)
        except:
            return {"message": gettext("algorithm_error_inserting"), 'status': 500}

        return {'message': gettext("algorithm_uploaded").format(algorithm_json['algorithm']), 'status': 200}


    # @classmethod
    # def delete(cls, name):
    #     algorithm = AlgorithmCollection.find_by_name(name)
    #     try:
    #         AlgorithmCollection.delete_algorithm(name)
    #         return {"message": gettext("algorithm_deleted")}, 200
    #     except:
    #         return {"message": gettext("item_not_found")}, 404

