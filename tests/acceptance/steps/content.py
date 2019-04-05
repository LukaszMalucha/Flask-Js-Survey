from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.map_page import MapPage
from tests.acceptance.page_model.signup_page import SignupPage
from tests.acceptance.page_model.suggest_page import SuggestPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@then('There are all questions shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    questions = [question for question in page.question]
    assert len(questions) == 5


@then('I can see there is a map on the page')
def step_impl(context):
    page = MapPage(context.driver)
    assert page.map_section.is_displayed()


@then('I can see there is a signup form on the page')
def step_impl(context):
    page = SignupPage(context.driver)
    assert page.form.is_displayed()


@then('I can see there is a login form on the page')
def step_impl(context):
    page = LoginPage(context.driver)
    assert page.form.is_displayed()


@then('The answer is "Suggested Machine Learning algorithms are: Naive Bayes & LinearSVC"')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.answer.text == "Suggested Machine Learning algorithms are: Naive Bayes & LinearSVC"

@then('Algorithm "(.*)" is shown in the table')
def step_impl(context, content):
    page = SuggestPage(context.driver)
    suggested_algorithm = [algo for algo in page.suggested_algorithm if algo.text == content]
    assert len(suggested_algorithm) > 0
    assert all([algo.is_displayed() for algo in suggested_algorithm])

