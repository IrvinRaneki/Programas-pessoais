import selenium
import webbrowser
from selenium import webdriver

web = webdriver.Firefox()
web.get("http://www.google.com")
driver.wait = WebDriverWait(driver, 2)
#webbrowser.open_new("http://www.google.com.br")

#box1 = web.find_element_by_name("q")
#box1.send_keys("ra")
