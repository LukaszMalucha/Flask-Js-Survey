from ma import ma
from models.algorithm import AlgorithmModel

class AlgorithmSchema(ma.ModelSchema):
    class Meta:
        model = AlgorithmModel
