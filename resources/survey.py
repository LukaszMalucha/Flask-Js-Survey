from flask import request, session
from flask_restful import Resource
from marshmallow import ValidationError
from libs.strings import gettext
from models.survey import SurveyModel
from libs.estimator import estimate_results, estimate_score



class Survey(Resource):
    @classmethod
    def get(cls):
        """Get survey Q & A"""
        message_success = session.get('message_success', None)  # Success login message
        session['message_success'] = None
        message_warning = session.get('message_warning', None)  # Warning message
        session['message_warning'] = None
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
