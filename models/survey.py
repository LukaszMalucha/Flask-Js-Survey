from db import mongo


class SurveyModel:

    def __init__(self):
        self.mongo = mongo


    @classmethod
    def find_all(cls):
        return mongo.db.Questions.find({})