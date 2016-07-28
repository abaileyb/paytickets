from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException   

from email_handler import *
from personal_info import paymentInfo
from personal_info import carInfo


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
select_veh_state.select_by_value(carInfo["state"])

enter_veh_plate = driver.find_element_by_id("veh_plate")
enter_veh_plate.send_keys(carInfo["plate"])

button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "continue")))
button.click()


# Second Page #

if(check_exists_by_xpath("/html/body/form/div[2]/div[1]/div[3]/strong", driver)):
	send_noTicketsFound_message()
	driver.close()

else:
	button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "button1id")))
	button.click()


# Third Page #
number_of_tickets = driver.find_element_by_xpath("/html/body/div[2]/div/form/div[3]/h4")
number_of_tickets = number_of_tickets.text.rsplit(None, 1)[-1]

total_amount = driver.find_element_by_xpath("/html/body/div[2]/div/form/div[5]/table/tbody/tr[3]/td[2]/span")
total_amount = total_amount.text

button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "pay")))
button.click()


# Fourth Page #
text_fields = ["name", "streetAddress", "city", "zipCode", "accountNumber", "cvv2", "email"]
for x in text_fields:
	enter = driver.find_element_by_name(x)
	enter.send_keys(paymentInfo[x])


select_fields = ["state", "month", "year"]
for x in select_fields:
	enter = Select(driver.find_element_by_name(x))
	enter.select_by_value(paymentInfo[x])

button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "continue")))
button.click()


# Fifth Page #
send_TicketsFound_message(number_of_tickets, total_amount)

button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "continue")))
button.click()

