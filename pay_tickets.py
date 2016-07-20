from selenium import webdriver
from selenium.webdriver.common.keys import Keys 



driver = webdriver.Firefox()    
driver.get("http://google.com/")
elem = driver.find_element_by_name("q")
elem.send_keys("lol goog lol")




	


driver.close()