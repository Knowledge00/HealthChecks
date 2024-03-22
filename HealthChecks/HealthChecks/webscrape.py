from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np
import sys
import time
import os
options = ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://riskscore.diabetes.org.uk/')
#driver.maximize_window()
wait = WebDriverWait(driver, 10)
name_of_program = sys.argv[0]
name1 = sys.argv[1]
consent_cb = sys.argv[2]
name_hc = sys.argv[3]
now = sys.argv[4]
location_hc = sys.argv[5]
phone = sys.argv[6]
email = sys.argv[7]
postcode = sys.argv[8]
gp_register = sys.argv[9]
gp = sys.argv[10]
sex1 = sys.argv[11]
age = sys.argv[12]
ethnicity1 = sys.argv[13]
dia_hist = sys.argv[14]
bp_hist = sys.argv[15]
waist = sys.argv[16]
height = sys.argv[17]
weight = sys.argv[18]



### COOKIES ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']"))).click()
time.sleep(1) 
### START ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='start-survey']"))).click()
time.sleep(1) 

### SEX ###

wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='%s']"%(sex1)))).click()
time.sleep(1) 

### AGE ###
wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="quiz_age"]'))).click()
time.sleep(1) 
age_box = driver.find_element(By.ID, "quiz_age")
age_box.send_keys(age)

driver.find_element(By.XPATH, "//button[@class='button next'][normalize-space()='Next']").click()
time.sleep(1) 

### ETHNICITY ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='%s']"%(ethnicity1)))).click()
time.sleep(1) 


### FIRST-ORDER DIABETIC ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='question current']//label[@class='button'][normalize-space()='%s']"%(dia_hist)))).click()
time.sleep(1) 


### WAIST ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='quiz_waistMeasurementUnits_1']"))).click() #units
time.sleep(1) 
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='quiz_waistCircumference']"))).click()
time.sleep(1) 
waist_value = driver.find_element(By.ID, "quiz_waistCircumference")
waist_value.send_keys(waist)

wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='container with-diagram']//button[@class='button next'][normalize-space()='Next']"))).click()
time.sleep(1) 


### BMI ###
wait.until(EC.element_to_be_clickable((By.ID, "quiz_heightMeasurementUnits_1"))).click()
time.sleep(1) 
wait.until(EC.element_to_be_clickable((By.ID, "quiz_heightMeasurementPrimary"))).click()
time.sleep(1) 
p_height_value = driver.find_element(By.ID, "quiz_heightMeasurementPrimary")
p_height_value.send_keys(height)


wait.until(EC.element_to_be_clickable((By.ID, "quiz_weightMeasurementUnits_1"))).click()
time.sleep(1) 
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='quiz_weightMeasurementPrimary']"))).click()
time.sleep(1) 
p_weight_value = driver.find_element(By.ID, "quiz_weightMeasurementPrimary")
p_weight_value.send_keys(weight)

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='bmi']")))
bmi_value = driver.find_element(By.XPATH, "//input[@name='bmi']").get_attribute('value')
print(bmi_value)
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='result']//div//button[@class='button next'][normalize-space()='Next']"))).click()
time.sleep(1) 

### HIGH BP ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='question current']//label[@class='button'][normalize-space()='%s']"%(bp_hist)))).click()
time.sleep(1) 

### NO THANKS ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'No thanks, I')]"))).click()
time.sleep(1) 

### RESULTS ###
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Restart the Diabetes UK Risk Tool']")))

age = driver.find_element(By.XPATH, "//body[1]/div[3]/form[1]/section[1]/div[2]/section[1]/div[2]/table[1]/tbody[1]/tr[1]/th[1]").text
age_score = driver.find_element(By.CLASS_NAME, "highlight").text
print(age_score)


Name = [name1]
HealthChampion = [name_hc]
DateOfHealthCheck = [now]
LocationOfHealthCheck = [location_hc]
PhoneNumber = [phone]
Postcode = [postcode]
EmailAddress = [email]
Name_of_GP = [gp]
Sex = [sex1]
Ethnicity = [ethnicity1]
Waist = [waist]
Height = [height]
Weight = [weight]
BMI = [bmi_value]
AgeScore = [age_score]
columns = ['Name', 'Health Champion', 'Date Of Health Check','Location Of Health Check', 'Phone number', 'Postcode', 'Email', 'GP', 'Sex', 'Ethnicity', 'Waist(cm)', 'Weight(cm)', 'Height(cm)', 'BMI', 'age_score' ]
def save_excel_sheet(df, excel_path, sheet_name):
    if not os.path.exists(excel_path):
        df.to_excel(excel_path, sheet_name=sheet_name, index=False)
    else:
        with pd.ExcelWriter(excel_path, engine='openpyxl', if_sheet_exists='overlay', mode='a') as writer:
            df.to_excel(writer, sheet_name=sheet_name, startrow=writer.sheets[sheet_name].max_row, header=None, index=False)

df = pd.DataFrame(list(zip(Name,HealthChampion,DateOfHealthCheck,LocationOfHealthCheck,PhoneNumber,postcode,EmailAddress,Name_of_GP,Sex,Ethnicity,Waist,Height, Weight,BMI, AgeScore)), columns=columns)
'''with pd.ExcelWriter('HealthChecks.xlsx',mode='a', engine="openpyxl") as writer:  
    df.to_excel(writer, sheet_name='Data')'''
save_excel_sheet(df, "HealthChecks.xlsx", sheet_name='Data')