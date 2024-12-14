from selenium import webdriver

class BrowserManager:
    browser = None
    @staticmethod
    def launchBrowser(browserName):
        try:
            browser_map = {
                "chrome": webdriver.Chrome,
                "firefox": webdriver.Firefox,
                "ie": webdriver.Ie
            }
            browser_selection = browser_map.get(browserName)
            if browser_selection is None:
                raise RuntimeError(f"Browser '{browserName}' not supported.")
            BrowserManager.browser = browser_selection()
        except Exception as e:
            raise RuntimeError(f"Error initializing the WebDriver: {e}")

        return BrowserManager.browser
