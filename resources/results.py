from flask import request, jsonify
from flask_restful import Resource

from libs.estimator import estimate_results, estimate_score


class Results(Resource):
    @classmethod
    def post(cls):
        answers = request.get_json()
        score = estimate_results(answers)
        result = estimate_score(score)
        result = ' & '.join(result)
        return jsonify({'result': result})
        # return {'result': result}  ???