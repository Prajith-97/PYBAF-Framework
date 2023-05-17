from behave import *


@given('user clicks on My Account button')
def click_forgotLink(context):
    try:
        context.objForgotPassword.click_myAccount()
    except Exception as e:
        context.exception = e


@when('user clicks on Login button')
def enter_name_forgot(context):
    try:
        context.objForgotPassword.click_login()
    except Exception as e:
        context.exception = e


@then('user can enter email id on login page')
def click_resetBtn(context):
    try:
        context.objForgotPassword.enterEmailID()
    except Exception as e:
        context.exception = e


# ------------------------------------------------------------------------

@when('user clicks on bus button')
def click_busBtn(context):
    try:
        context.objForgotPassword.clickBusBtn()
    except Exception as e:
        context.exception = e


@when('user press search bus button')
def click_searchBusBtn(context):
    try:
        context.objForgotPassword.clickSearchBusBtn()
    except Exception as e:
        context.exception = e


@then('redirected to search listing page')
def searchListingPage(context):
    try:
        stepName = context.step.name
    except Exception as e:
        context.exception = e
