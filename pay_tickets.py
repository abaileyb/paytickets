from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException   


## Helpers

def check_exists_by_xpath(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True



driver = webdriver.Firefox()    
driver.get("https://www.parkingticketpayment.com/ticketpay/index.php?imsvil=5A")

# First Page #
select_veh_state = Select(driver.find_element_by_id("veh_state"))
select_veh_state.select_by_value("NY")

enter_veh_plate = driver.find_element_by_id("veh_plate")
enter_veh_plate.send_keys('GTE2801')

button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "continue")))
button.click()


#Second Page #

if(check_exists_by_xpath("/html/body/form/div[2]/div[1]/div[3]/strong", driver)):
	driver.close()







