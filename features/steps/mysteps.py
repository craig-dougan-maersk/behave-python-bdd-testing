# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
import requests

@given('We have some tests to run')
def step_impl(context):
  pass

@when('we have no reason not to test')
def step_impl(context):
    assert True is not False

@then('The website "{url}" is up and reporting a "{status_code}" code.')
def step_impl(context, url, status_code):
  desired_status_code = status_code
  res = requests.get(url,allow_redirects=False)
  received_status_code = res.status_code
  assert int(desired_status_code) == int(received_status_code)

