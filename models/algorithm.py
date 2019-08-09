from db import mongo


class AlgorithmModel:

    def __init__(self):
        self.mongo = mongo

    def insert_algorithm(self, algorithm):
        return mongo.db.suggested_algorithms.insert_one(algorithm)

    def delete_algorithm(self, _id):
        mongo.db.suggested_algorithms.remove({'_id': _id})

    @classmethod
    def find_all(cls):
        return mongo.db.suggested_algorithms.find({})

    @classmethod
    def find_by_name(cls, name):
        return mongo.db.suggested_algorithms.find_one({'algorithm': name})


# {
#     "_id": {
#         "$oid": "5d0948ab4506d900047d4201"
#     },
#     "algorithm": "test", !!!!!!!!!!!!!!!!!!!!!!!!!!! ZAMIENIC NA NAME
#     "description": "test"
# }