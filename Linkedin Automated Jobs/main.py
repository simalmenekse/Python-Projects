from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = #YOUR EMAIL
ACOOUNT_PASSWORD = #YOUR PASSWORD
PHONE = #YOUR PHONE

chrome_driver_path = "C:\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3358739551&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in_button = driver.find_element_by_link_text("Oturum aç")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACOOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

time.sleep(5)
#phone = driver.find_element_by_id("single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3358739551-74680442-phoneNumber-nationalNumber")
#if phone.text == "":
#    phone.send_keys(PHONE)

submit_button = driver.find_element_by_id("ember411")
submit_button.click()
