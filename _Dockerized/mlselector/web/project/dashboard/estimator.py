## Assign specific estimators to the given scores

def estimate_score(score):
    if score in (11111, 11121):
        result = ['Naive Bayes', 'LinearSVC']
    elif score in (11112, 11122):
        result = ['KNeighbors Classifier', 'Kernel SVC', 'RandomForest Classifier']
    elif score in (11211, 11222, 11221, 11212):
        result = ["SGD Classifier", "Kernel Approximation"]
    elif score in (12112, 12111):
        result = ["KMeans-Classifier", "GMM"]
    elif score in (12212, 12211):
        result = ["MiniBatch KMeans"]
    elif score in (12121, 12122):
        result = ["Get more data"]
    elif score in (12221, 12222):
        result = ["MeanShift", "VBGMM"]
    elif score in (21212, 21221, 21222, 21211, 22211, 22212, 22221, 22222):
        result = ["SGD Regressor"]
    elif score in (21112, 21121, 21122, 21111, 22111, 22112, 22121, 22122):
        result = ["ElasticNet", "Kernel SVR", "RandomForest Regressor"]
    elif score in (31111, 31112, 31122, 31121, 32111, 32112, 32122, 32121):
        result = ["Kernel PCA", "Linear Discriminant Analysis"]
    elif score in (31211, 31212, 31222, 31221, 32211, 32212, 32222, 32221):
        result = ["Isomap", "Spectral Embedding"]
    else:
        result = ["Not all the questions were answered"]
    return result


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)


test_are_equal(estimate_score(21111), estimate_score(22111))
test_are_equal(estimate_score(31211), estimate_score(32221))

test_not_equal(estimate_score(31211), estimate_score(31111))
test_not_equal(estimate_score(21112), estimate_score(21212))
test_not_equal(estimate_score(12212), estimate_score(12112))
test_not_equal(estimate_score(11111), estimate_score(32121))

test_are_equal(estimate_score(31211), ["Isomap", "Spectral Embedding"])
test_are_equal(estimate_score(0), ["Not all the questions were answered"])
test_are_equal(estimate_score(11), ["Not all the questions were answered"])
test_are_equal(estimate_score(111), ["Not all the questions were answered"])
test_are_equal(estimate_score(1111), ["Not all the questions were answered"])


def estimate_results(answers):
    score = 0
    for question, user_answer in answers.items():
        if user_answer == 'I will categorize my data':
            score += 10000
        elif user_answer == 'I will be working with numerical data':
            score += 20000
        elif user_answer == 'I am not sure yet, just looking':
            score += 30000
        elif user_answer == 'Already labelled':
            score += 1000
        elif user_answer == 'Not labelled yet':
            score += 2000
        elif user_answer == 'Less than 100K':
            score += 100
        elif user_answer == 'More than 100K':
            score += 200
        elif user_answer == 'Already known':
            score += 10
        elif user_answer == 'I will have to figure it out':
            score += 20
        elif user_answer == 'Text data':
            score += 1
        elif user_answer == 'Other':
            score += 2
        else:
            score += 0
    return score
