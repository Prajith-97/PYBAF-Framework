from behave import *


@given('user is on the homepage')
def launchHomepage(context):
    try:
        context.objLink.launch_Homepage()
    except Exception as e:
        context.exception = e


@when('user clicks on holiday button')
def click_forgotPassword_link(context):
    try:
        context.objLink.click_holidayBtn()
    except Exception as e:
        context.exception = e


@when('user clicks on search holidays button')
def enter_username(context):
    try:
        context.objLink.click_searchHolidayBtn()
    except Exception as e:
        context.exception = e


@then('redirected to holiday search listing page')
def click_resetPassword_button(context):
    try:
        context.objLink.holiday_SLP()
    except Exception as e:
        context.exception = e


@then('user scrolls the page')
def scrollPage(context):
    try:
        context.objLink.scrollSLP()
    except Exception as e:
        context.exception = e
