from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options = Options()
binary = FirefoxBinary()
#browser = webdriver.Firefox(firefox_binary=binary)
browser = webdriver.Chrome()
browser.get('http://reddit.com/r/learnpython/new')

elem = browser.find_elements_by_css_selector('li.first')
links = elem.get_attribute("href")
elem.Close()
