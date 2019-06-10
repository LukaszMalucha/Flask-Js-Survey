from behave import *
from selenium import webdriver

from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.map_page import MapPage
from tests.acceptance.page_model.register_page import SignupPage
from tests.acceptance.page_model.add_algorithm_page import SuggestPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')   ## path to chromedriver
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the map page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = MapPage(context.driver)
    context.driver.get(page.url)

@given('I am on the signup page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = SignupPage(context.driver)
    context.driver.get(page.url)

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = LoginPage(context.driver)
    context.driver.get(page.url)


@given('I am on the suggest page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = SuggestPage(context.driver)
    context.driver.get(page.url)



@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the signup page')
def step_impl(context):
    expected_url = SignupPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the login page')
def step_impl(context):
    expected_url = LoginPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the map page')
def step_impl(context):
    expected_url = MapPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the suggest page')
def step_impl(context):
    expected_url = SuggestPage(context.driver).url
    assert context.driver.current_url == expected_url













