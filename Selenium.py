from selenium import webdriver
import time
from chromedriver_py import binary_path  # this will get you the path variable
driver = webdriver.Chrome(executable_path=binary_path)
# driver.fullscreen_window()

# driver.get('http://www.google.com/');
# time.sleep(5)  # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver\n')
# #search_box.submit()
# time.sleep(5)  # Let the user actually see something!
# driver.quit()

driver.get('http://www.google.com/')
elments = driver.find_elements_by_tag_name('a')
for elment in elments:
    if 'Gmail' in elment.text:
        elment.click()

elments = driver.find_elements_by_tag_name('a')
for elment in elments:
    if 'Sign in' in elment.text:
        elment.click()