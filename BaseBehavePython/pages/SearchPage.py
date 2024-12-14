from selenium.webdriver.common.by import By

from BaseBehavePython.pages.BasePage import BasePage
from BaseBehavePython.utilities import configReader


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    pageTitle = (By.XPATH, "//*[@alt='Google']")
    inputTextLabel = (By.XPATH, "(//input[@value='Google Search'])[2]")

    def launchApplication(self):
        x = configReader.read_configuration("basic info", "url")
        self.driver.get(configReader.read_configuration("basic info", "url"))

    def verifyPageTitle(self):
        actualValue = self.webElement_getAttribute(self.pageTitle, "alt")
        assert "Google".__eq__(actualValue)

    def verify_inputTextlabel_isDisplayed(self):
        assert self.webElement_isDisplayed(self.inputTextLabel)