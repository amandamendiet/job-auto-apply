from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dotenv
import os

dotenv.load_dotenv()

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4092320928&distance=25&f_AL=true&f_E=1%2C2&f_WT=2&geoId=103644278&keywords=python%20developer%20remote&origin=JOB_SEARCH_PAGE_JOB_FILTER"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)
driver.maximize_window()

# click sign in
sign_in = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='base-contextual-sign-in-modal']/div/section/div/div/div/div[2]/button"))
)
sign_in.click()

# input username and password
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='base-sign-in-modal_session_key']"))
)
username.send_keys(USERNAME)

password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='base-sign-in-modal_session_password']"))
)
password.send_keys(PASSWORD)

send = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='base-sign-in-modal']/div/section/div/div/form/div[2]/button"))
)
send.click()

