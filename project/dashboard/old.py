from flask import render_template, redirect, url_for, request, Blueprint, session
from bson.objectid import ObjectId

from .estimate import estimate_score, results

## Blueprint Init

dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder="templates"
    )

from app import mongo




########################################################################## MAIN DASHBOARD ###################################################################################################################    


## MAIN DASHBOARD #######################################################

@dashboard_blueprint.route('/', methods=['GET', 'POST'])
# @dashboard_blueprint.route('/dashboard')
def dashboard():
    questions=mongo.db.Questions.find()
    result = []
    message = 'Please answer all the questions'
    
    if request.method == 'POST':
        answers = request.form 
        score = results(answers)

        


## Assign specific estimators to the given scores:
        result = estimate_score(score) 
        algos = ' & '.join(result)
        message = 'Suggested Machine Learning algorithms are: {}'.format(algos)
           
        
    return render_template('dashboard.html', questions=questions, result = result, message = message)
    
    
    
####################################################################### Adding algorithms ################################################################################################################################


## ROUTES - Suggest Algorithm:

@dashboard_blueprint.route('/add_algorithm')
def add_algorithm():
    suggested_algorithms = mongo.db.suggested_algorithms.find()
    
    return render_template('add_request.html', suggested_algorithms = suggested_algorithms)


## ROUTES - Save Algorithm:

@dashboard_blueprint.route('/insert_algorithm', methods=['POST'])
def insert_algorithm():
    suggested_algorithms =  mongo.db.suggested_algorithms
    suggested_algorithms.insert_one(request.form.to_dict())
    return redirect(url_for('dashboard.add_algorithm'))
    
## ROUTES - Delete Algorithm:    
    
@dashboard_blueprint.route('/delete_algorithm/<algorithm_id>')
def delete_algorithm(algorithm_id):
    mongo.db.suggested_algorithms.remove({'_id': ObjectId(algorithm_id)})
    return redirect(url_for('dashboard.add_algorithm'))    
    
    
## ROUTES - SciKit Map:      

@dashboard_blueprint.route('/map')
def map():
    return render_template('map.html')