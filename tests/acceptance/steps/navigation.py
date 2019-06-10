from behave import *
from selenium import webdriver

from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.map_page import MapPage
from tests.acceptance.page_model.register_page import RegisterPage
from tests.acceptance.page_model.add_algorithm_page import AddAlgorithmPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('chromedriver')  # path to chromedriver
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the map page')
def step_impl(context):
    context.driver = webdriver.Chrome('chromedriver')
    page = MapPage(context.driver)
    context.driver.get(page.url)


@given('I am on the register page')
def step_impl(context):
    context.driver = webdriver.Chrome('chromedriver')
    page = RegisterPage(context.driver)
    context.driver.get(page.url)


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome('chromedriver')
    page = LoginPage(context.driver)
    context.driver.get(page.url)


@given('I am on the add algorithm page')
def step_impl(context):
    context.driver = webdriver.Chrome('chromedriver')
    page = AddAlgorithmPage(context.driver)
    context.driver.get(page.url)


###########################################################

@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the register page')
def step_impl(context):
    expected_url = RegisterPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the login page')
def step_impl(context):
    expected_url = LoginPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the map page')
def step_impl(context):
    expected_url = MapPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the add algorithm page')
def step_impl(context):
    expected_url = AddAlgorithmPage(context.driver).url
    assert context.driver.current_url == expected_url
