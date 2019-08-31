from db import mongo


class AlgorithmCollection:

    def __init__(self):
        self.mongo = mongo

    def insert_algorithm(self, algorithm):
        return mongo.db.suggested_algorithms.insert(algorithm)

    def delete_algorithm(self, name):
        mongo.db.suggested_algorithms.remove({'name': name})

    @classmethod
    def find_all(cls):
        return mongo.db.suggested_algorithms.find({})

    @classmethod
    def find_by_name(cls, name):
        return mongo.db.suggested_algorithms.find_one({'name': name})
