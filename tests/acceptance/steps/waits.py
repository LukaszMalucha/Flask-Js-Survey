from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from tests.acceptance.locators.base_page import BasePageLocators

use_step_matcher('re')


@given('I wait for the page to load')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.PAGE)
    )

@given('I wait for the dropdown to load')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.DROPDOWN)
    )

@when('I wait for a second')
def step_impl(context):
    time.sleep(1)