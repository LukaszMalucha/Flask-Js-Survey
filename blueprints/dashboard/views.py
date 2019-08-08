from flask import render_template, redirect, url_for, request, Blueprint, jsonify
from bson import ObjectId
from libs.estimator import estimate_score, estimate_results

# Blueprint Init

dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder="templates"
)

from app import mongo


# MAIN DASHBOARD

@dashboard_blueprint.route('/', methods=['GET', 'POST'])
def dashboard():
    question_query = mongo.db.Questions.find({})
    answers = []
    questions = []
    for element in question_query:
        questions.append(element['question'])
        answers.append(element['answers'])

    return render_template('dashboard.html', questions=questions, answers=answers)


@dashboard_blueprint.route('/results', methods=['POST'])
def results():
    answers = request.get_json()
    score = estimate_results(answers)
    result = estimate_score(score)
    result = ' & '.join(result)
    return jsonify({'result': result})


# ROUTES - Suggest Algorithm:

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


# ROUTES - SciKit Map:

@dashboard_blueprint.route('/map')
def map():
    return render_template('map.html')
