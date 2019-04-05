# ML Selector Project

[Visit App on Heroku](https://mlselector.herokuapp.com/)


## PROJECT CASE:

How do I know which method of parameter estimation to choose? <br>

It's hard to decide if you have so many different algorithms to your disposal. But with certain information given about analysed dataset, we can narrow that choice to few best matches.


## GOAL STATEMENT:
Goal of the project is to create survey, that will help to decide which ML algorithm is the most suitable one for a given task.

## PROJECT REQUIREMENTS:
1.	Application must enter their answers & submit it using form.
2.	Suggested algorithms and descriptions(instead of q & a) are stored and accessible (MongoDB)
2.	Users have to be identifiable by unique username/password (SqlAlchemy database has been implemented)
3.	App must be written in Python. HTML, CSS, and JavaScript
4.	App should be built with TDD approach
5.	Flask framework should be used 
6.	App should be responsive
7.	Apply Responsive Design

## APP STRUCTURE

#### Main Dashboard View:

![mls1](https://user-images.githubusercontent.com/26208598/41541629-d5c90be8-730a-11e8-8a9b-6c5584919855.JPG)

1. Dataset Form - requires User input in order to match ML estimator

2. Match Estimator Button - press to process a form

3. Login/Registry Menu - shows "Guest" when user is not logged in.

4. ML Library Button - link to 

5. Suggest Button - brings User to "Add Algorithm" menu

6. Scikit Map Button - brings full map of ML Estimators


#### Add Algorithm View:

![mls2](https://user-images.githubusercontent.com/26208598/41541630-d6e515d0-730a-11e8-9269-42f598dc0149.JPG)

1. Add Algorithm Card - User can suggest new algorithm for ML Estimator

2. User Suggestions Table - Table of current ML Estimator proposals 
## Test Suite:

### Travis CI
[![Build Status](https://travis-ci.org/LukaszMalucha/PP-Milestone-Project.svg?branch=master)](https://travis-ci.org/LukaszMalucha/PP-Milestone-Project)

### Test Files

#### /tests
Views unit tests

#### test_score.py
Estimator algorithm test

### Manual Tests:

### Login/Signin Form Test:
1. Is data properly saved in database
2. Are different templates properly routing to signup and login urls
3. Are form fields values properly validated (example: email field)
4. Is password properly hashed

### Score assigner:
1. Is correct score assign to certain answer
2. If no answer is marked then survey result should be "Not all the questions were answered"

### Estimate.py
1. Standard assertion tests within file 

### Data-Questions:
1. Are data questions properly displayed

### Results:
1. Are estimator field properly displayed

### Add suggestion
1. Testing various inputs and datatable functionality

### App Responsivity: 
1. Done with Inspect element tool as a last part of the test suite




## Tools, Modules and Techniques:


##### Web Development:
Flask | Docker | Heroku | Bootstrap | Materialize | DataTables.js

##### Database

MongoDB | Sqlite

##### Testing

Selenium | UnitTest



## CREDITS & INSPIRATIONS

#### scikit-learn source

http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

#### Error 404 template:

Robin Selmer:

https://codepen.io/robinselmer/pen/vJjbOZ



Thank you,

Lukasz Malucha