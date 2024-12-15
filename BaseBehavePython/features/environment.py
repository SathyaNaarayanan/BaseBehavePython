import logging
from sys import exception
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.selenium_manager import logger
from selenium.webdriver.remote.webdriver import WebDriver
from BaseBehavePython.utilities.BrowserManager import BrowserManager
from BaseBehavePython.utilities.DriverManager import DriverManager
from BaseBehavePython.utilities import configReader


#hooks
def before_all(context):
    context.logger = logger_Predefined("BaseBehavePython","LYFnGO-Logger")

def before_scenario(context, scenario):
    try:
        # browser = configReader.read_configuration("basic info", "browser").lower()
        context.driver: WebDriver = driver_initialization(getBrowser())
        context.driver.maximize_window()
        launchApplication(context.driver, getApplicationURL())
    except Exception as e:
        context.logger.error(f"ERROR : {str(e)}")
        raise

def before_step(context, step):
    try:
        context.logger.info(f"function step started: {step.name}")
    except exception as e:
        context.logger.error(f"ERROR : {str(e)}")
        raise


def after_step(context, step):
    try:
        if step.status == "passed":
            context.logger.info(f"function step passed: {step.name}")
            allure.attach(context.driver.get_screenshot_as_png()
                          , name="passed_screenshot"
                          , attachment_type=AttachmentType.PNG)
        elif step.status == "failed":
            context.logger.info(f"function step failed: {step.name}")
            allure.attach(context.driver.get_screenshot_as_png()
                          , name="failed_screenshot"
                          , attachment_type=AttachmentType.PNG)
    except Exception as e:
        context.logger.error(f"ERROR : {str(e)}")
        raise


def after_scenario(context, scenario):
    driver_close(context.driver)

def driver_initialization(browser):
    try:
        driver = DriverManager.get_driverInstance().set_driver(BrowserManager.launchBrowser(browser))
        driver: WebDriver = DriverManager.get_driverInstance().get_driver()
        return driver
    except Exception as e:
        logger.error(f"ERROR : {str(e)}")
        raise

def getApplicationURL():
    return configReader.read_configuration("basic info", "url")

def getBrowser():
    return configReader.read_configuration("basic info", "browser").lower()

def launchApplication(driver, url):
    try:
        driver.get(url)
    except Exception as e:
        logger.error(f"ERROR : {str(e)}")
        raise

def driver_close(driver):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(f"Error quitting driver: {e}")
        finally:
            driver = None

def logger_Predefined(filepath, filename):
    logger = logging.getLogger(filepath+'/'+filename)
    logger.setLevel(logging.INFO)

    # existing logs will be removed
    with open(filepath+'/'+filename+'.log', 'w'):
        pass

    # file Handler - for new logs
    file_handler = logging.FileHandler(filepath+'/'+filename+'.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    return logger

