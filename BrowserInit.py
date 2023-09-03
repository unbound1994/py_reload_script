from selenium import webdriver


class BrowserInit:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--start-maximized')
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_experimental_option("detach", True)  # TODO delete after iteration!
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def initialization_browser(self):
        yield self.driver
        print("\nquit browser..")
        self.driver.quit()
        self.driver.close()
