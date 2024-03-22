
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import time

def edientry(age_group, sex, ethnicity):
    options = ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get('https://forms.office.com/e/LT7NGzzrFB')
    wait = WebDriverWait(driver, 10)

# Age
    if age_group == '18-30':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(2) > div.-dq-42 > div > div > div:nth-child(1)'))).click()
    elif age_group == '31-40':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(2) > div.-dq-42 > div > div > div:nth-child(2)'))).click()
    elif age_group == '41-50':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(2) > div.-dq-42 > div > div > div:nth-child(3)'))).click()
    elif age_group == '51-60':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(2) > div.-dq-42 > div > div > div:nth-child(4)'))).click()
    elif age_group == '61-70':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(2) > div.-dq-42 > div > div > div:nth-child(5)'))).click()
    elif age_group == '71-80':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(2) > div.-dq-42 > div > div > div:nth-child(6)'))).click()
    elif age_group == '80+':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(2) > div.-dq-42 > div > div > div:nth-child(7)'))).click()

# Sex
    if sex == 'Male':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(3) > div.-dq-42 > div > div > div:nth-child(1)'))).click()
    elif sex == 'Female':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(3) > div.-dq-42 > div > div > div:nth-child(2)'))).click()
    
# Gender
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(4) > div.-dq-42 > div > div > div:nth-child(1)'))).click()

# Ethnicity
    if ethnicity == 'White – British':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(1)'))).click()
    elif ethnicity == 'White – Irish':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(2)'))).click()
    elif ethnicity == 'White – Any other White background':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(3)'))).click()
    elif ethnicity == 'Asian or Asian British – Indian':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(4)'))).click()
    elif ethnicity == 'Asian or Asian British – Pakistani':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(5)'))).click()
    elif ethnicity == 'Asian or Asian British – Bangladeshi':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(6)'))).click()
    elif ethnicity == 'Asian or Asian British - Any other Asian background':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(7)'))).click()
    elif ethnicity == 'Black or Black British – Caribbean':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(8)'))).click()
    elif ethnicity == 'Black or Black British – African':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(9)'))).click()
    elif ethnicity == 'Black or Black British - Any other Black background':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(10)'))).click()
    elif ethnicity == 'Other Ethnic Groups – Chinese':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(5) > div.-dq-42 > div > div > div:nth-child(11)'))).click()
    else:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Other']"))).send_keys(ethnicity)

# UK
    if uk_born == 'Yes':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(6) > div.-dq-42 > div > div > div:nth-child(1)'))).click()
    elif uk_born == 'No':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(6) > div.-dq-42 > div > div > div:nth-child(2)'))).click()

# YEARS
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='The value must be a number']"))).send_keys(uk_years)

# LANGUAGE
    if first_english == 'Yes':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(8) > div.-dq-42 > div > div > div:nth-child(1)'))).click()
    elif first_english == 'No':
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#question-list > div:nth-child(8) > div.-dq-42 > div > div > div:nth-child(2)'))).click()

# 





        
        
    time.sleep(10)

edientry('41-50', 'Female', 'Asian or Asian British – Pakistani')
