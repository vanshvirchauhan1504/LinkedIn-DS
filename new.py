from linkedin_scraper import Person, actions
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(chrome_options)

email = "harsh.sharma.test1@gmail.com"
password ="test@link.123"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/vanshvirchauhan1504/", driver=driver)

print(person)
