from ma import ma
from models.survey import SurveyModel

class SurveySchema(ma.ModelSchema):
    class Meta:
        model = SurveyModel