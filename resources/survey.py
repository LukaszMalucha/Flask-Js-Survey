from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from libs.strings import gettext
from models.survey import SurveyModel
from schemas.survey import SurveySchema
from libs.estimator import estimate_results, estimate_score

survey_list_schema = SurveySchema(many=True)


class Survey(Resource):
    @classmethod
    def get(cls):
        """Get survey Q & A"""
        survey = SurveyModel.find_all()
        answers = []
        questions = []
        for element in survey:
            questions.append(element['question'])
            answers.append(element['answers'])

        return {'questions': questions, 'answers': answers}

    @classmethod
    def post(cls):
        """Post survey results"""
        answers = request.get_json()
        score = estimate_results(answers)
        result = estimate_score(score)
        result = ' & '.join(result)
        return {'result': result}
