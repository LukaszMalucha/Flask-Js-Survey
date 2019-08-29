from flask import request, Response, render_template
from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required
from marshmallow import ValidationError
from libs.strings import gettext
from models.algorithm import AlgorithmModel
# from schemas.algorithm import AlgorithmSchema

# algorithm_schema = AlgorithmSchema()
# algorithm_list_schema = AlgorithmSchema(many=True)


class Algorithms(Resource):

    @classmethod
    def get(cls):
        suggested_algorithms = AlgorithmModel.find_all(cls)
        return Response (render_template('algorithms.html', suggested_algorithms=suggested_algorithms))

    # @classmethod
    # def post(cls, name):
    #     if AlgorithmModel.find_by_name(name):
    #         return {"message": gettext("algorithm_name_exists").format(name)}, 400
    #
    #     algorithm_json = request.get_json()
    #
    #     algorithm = algorithm_schema.load(algorithm_json)
    #
    #     try:
    #         AlgorithmModel.insert_algorithm(algorithm_json)
    #     except:
    #         return {"message": gettext("algorithm_error_inserting")}, 500
    #
    #     return algorithm_schema.dump(algorithm), 201
    #
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
