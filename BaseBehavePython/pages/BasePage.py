from encodings.punycode import selective_find

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def webElement_click(self,elementLocator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((elementLocator)))
        self.getElement(elementLocator).click()

    def webElement_inputText(self,elementLocator, inputText):
        element = self.getElement(elementLocator)
        element.click()
        element.clear()
        element.send_keys(inputText)

    def webElement_isDisplayed(self,elementLocator):
        return self.getElement(elementLocator).is_displayed()

    def webElement_explicitWait(self, elementLocator):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((elementLocator)))
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((elementLocator)))


    def webElement_getText(self,elementLocator):
        return self.getElement(elementLocator).text

    def webElement_getAttribute(self,elementLocator, attributeKey) -> str:
        return self.getElement(elementLocator).get_attribute(attributeKey)

    def getElement(self, elementLocator):
        self.webElement_explicitWait(elementLocator)
        elementType = self.driver.find_element(*elementLocator)
        """(*locator) is to unpack the tuple into 2 separate aruguments"""
        return elementType

    def webElement_isEnabled(self, elementLocator):
        return self.getElement(elementLocator).is_enabled()

    def webElement_isSelected(self, elementLocator):
        return self.getElement(elementLocator).is_selected()

    def webElement_submit(self, elementLocator):
        return self.getElement(elementLocator).submit()

    def base_uploadFile(self, elementLocator, fileLocation):
        self.getElement(elementLocator).send_keys(fileLocation)

    def base_driverRefresh(self):
        self.driver.refresh()

    def base_driverForward(self):
        self.driver.forward()

    def base_driverBack(self):
        self.driver.back()

    def base_simpleAlert(self, elementLocator):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.getElement(elementLocator).click()
        self.driver.switch_to.alert.accept()

    def base_acceptConfirmationAlert(self, elementLocator):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.getElement(elementLocator).click()
        self.driver.switch_to.alert.accept()

    def base_dismissConfirmationAlert(self, elementLocator):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.getElement(elementLocator).click()
        self.driver.switch_to.alert.dismiss()

    def base_promptalert(self, elementLocator, inputText):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.getElement(elementLocator).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(inputText)
        alert.accept()





