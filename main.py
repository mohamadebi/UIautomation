from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Specify the path to the downloaded ChromeDriver executable
chrome_driver_path = '/home/mohamad/Desktop/chromedriver-linux64/chromedriver'
# Create a new instance of the Chrome driver using the specified path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)



driver.get("http://google.com")
search_box = driver.find_element('name', 'q')
time.sleep(3)
search_box.send_keys('varzesh3')
time.sleep(3)
search_box.send_keys("Return")
time.sleep(3)

driver.quit()
