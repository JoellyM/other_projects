import selenium.webdriver

options = selenium.webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = selenium.webdriver.Firefox(firefox_options=options)
driver.get('https://www.python.org/')
print(driver.title)

