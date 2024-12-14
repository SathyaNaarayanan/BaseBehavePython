import time

from behave import *

from BaseBehavePython.pages.SearchPage import SearchPage


@given(u'Launched LfynGo login page')
def launched_LfynGo_login_page(context):
    try:
        context.logger.info("Google Launched launched")
        context.searchPage = SearchPage(context.driver)
        context.searchPage.launchApplication()
        context.searchPage.verifyPageTitle()
        time.sleep(5)
        print("applicaiton launched")
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")
        raise

@given(u'Launch Google chrome website')
def step_impl(context):
    try:
        context.logger.info("Google Launched launched")
        context.searchPage = SearchPage(context.driver)
        context.searchPage.verifyPageTitle()
        print("applicaiton launched")
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")
        raise


@then(u'verify google search button')
def step_impl(context):
    try:
        context.logger.info("Verify input text label")
        context.searchPage.verify_inputTextlabel_isDisplayed()
    except Exception as e:
        context.logger.error(f"FAILED --->  ERROR : {str(e)}")
        raise