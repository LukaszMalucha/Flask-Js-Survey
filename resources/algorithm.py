from flask import request, Response, render_template
from flask_restful import Resource
from marshmallow import ValidationError
from libs.strings import gettext
from models.algorithm import AlgorithmModel


class Algorithms(Resource):

    @classmethod
    def get(cls):
        suggested_algorithms = AlgorithmModel.find_all()
        return Response(render_template('algorithms.html', suggested_algorithms=suggested_algorithms))

    @classmethod
    def post(cls):

        algorithm = request.get_json()
        # data = {}
        # data['algorithm'] = algorithm_json['algorithm']
        # data['candidates'] = candidates_data
        # if AlgorithmModel.find_by_name(algorithm_json['algorithm']):
        #     return {"message": gettext("algorithm_name_exists").format(algorithm_json['algorithm']), 'status': 400}
        #
        # try:
        #     AlgorithmModel.insert_algorithm(algorithm_json)
        # except:
        #     return {"message": gettext("algorithm_error_inserting"), 'status': 500}
        #
        # return {'message': gettext("algorithm_uploaded").format(algorithm_json['algorithm']), 'status': 400}
        mongodb = AlgorithmModel()
        mongodb.insert_algorithm(algorithm)
    # @classmethod
    # def delete(cls, name):
    #     algorithm = AlgorithmModel.find_by_name(name)
    #     try:
    #         AlgorithmModel.delete_algorithm(name)
    #         return {"message": gettext("algorithm_deleted")}, 200
    #     except:
    #         return {"message": gettext("item_not_found")}, 404

# class AlgorithmList(Resource):
#     @classmethod
#     def get(cls):
#         return {"algorithms": algorithm_list_schema.dump(AlgorithmModel.find_all())}, 200
