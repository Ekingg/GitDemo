from selenium import webdriver
from chromedriver_py import binary_path  # this will get you the path variable
driver = webdriver.Chrome(executable_path=binary_path)
# driver.fullscreen_window()

driver.get('http://www.google.com/');
#time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
#time.sleep(5)  # Let the user actually see something!
driver.quit()
