from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required
from marshmallow import ValidationError
from libs.strings import gettext
from models.algorithm import AlgorithmModel
from schemas.algorithm import AlgorithmSchema

algorithm_schema = AlgorithmSchema()
algorithm_list_schema

class AlgorithmList(Resource):
    @classmethod
    def get(cls):
        return {"algorithms": }









@dashboard_blueprint.route('/add_algorithm')
def add_algorithm():
    suggested_algorithms = mongo.db.suggested_algorithms.find()

    return render_template('add_request.html', suggested_algorithms=suggested_algorithms)


# ROUTES - Save Algorithm:

@dashboard_blueprint.route('/insert_algorithm', methods=['POST'])
def insert_algorithm():
    suggested_algorithms = mongo.db.suggested_algorithms
    suggested_algorithms.insert_one(request.form.to_dict())
    return redirect(url_for('dashboard.add_algorithm'))


# ROUTES - Delete Algorithm:

@dashboard_blueprint.route('/delete', methods=['DELETE'])
def delete():
    algorithm_id = request.form['id']
    mongo.db.suggested_algorithms.remove({'_id': ObjectId(algorithm_id)})
    return jsonify({'id': algorithm_id})


