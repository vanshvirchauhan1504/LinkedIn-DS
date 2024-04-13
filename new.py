from linkedin_scraper import Person, actions
from selenium import webdriver

# email = "some-email@email.address"
# password = "password123"
# chrome_options.add_argument("--ignore-certificate-errors")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(chrome_options)


email = "vanshvirchauhan1504@gmail.com"
password ="Vansh@181075"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/vidhichadha/", driver=driver)