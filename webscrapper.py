from selenium import webdriver
from selenium.webdriver.support.select import Select
from captcha import captcha_solver
import time

url="https://electoralsearch.in/"

#start scraping
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url)

#click on continue button at startup
cont_tab_id = 'continue'
cont_tab = driver.find_element_by_id(cont_tab_id)
cont_tab.click()


#Selecting tab2
tab1=driver.find_element_by_css_selector("li[role='tab']")
driver.execute_script("arguments[0].setAttribute('class','')", tab1)
driver.execute_script("arguments[0].setAttribute('role','')", tab1)

tab2=driver.find_element_by_css_selector("li[role='tab']")
driver.execute_script("arguments[0].setAttribute('class','active')", tab2)
tab2.click()  

                                          
#Filling form values
driver.find_element_by_id('name').send_keys('MZH2380426')

select = Select(driver.find_element_by_xpath('//*[@id="epicStateList"]'))

driver.find_element_by_id("captchaEpicImg").screenshot('captcha.png')

time.sleep(2)

stateValue = "Haryana"
for option in select.options:
    value = option.get_attribute('value')
    if stateValue == value:
        option.click()
        break

captcha_text=captcha_solver.get_captcha_text().replace(" \r\n","").replace(" ","")

driver.find_element_by_id('txtEpicCaptcha').send_keys(captcha_text)

#click on search button
driver.find_element_by_id('btnEpicSubmit').click()

# sleep processing till detalis loads
time.sleep(10)

#create csv file contains Voter information
record=[]

c_id=driver.find_element_by_css_selector("input[class='idInRow']").get_attribute('value')
epic_no=driver.find_element_by_css_selector("input[class='epicNoInRow']").get_attribute('value')
name=driver.find_element_by_css_selector("input[name='name'][type='hidden']").get_attribute('value')
gender=driver.find_element_by_css_selector("input[name='gender']").get_attribute('value')
age=driver.find_element_by_css_selector("input[name='age']").get_attribute('value')
rln_name=driver.find_element_by_css_selector("input[name='rln_name']").get_attribute('value')
last_update=driver.find_element_by_css_selector("input[name='last_update']").get_attribute('value')
state=driver.find_element_by_css_selector("input[name='state']").get_attribute('value')
district=driver.find_element_by_css_selector("input[name='district']").get_attribute('value')
ac_name=driver.find_element_by_css_selector("input[name='ac_name']").get_attribute('value')
ac_no=driver.find_element_by_css_selector("input[name='ac_no']").get_attribute('value')
pc_name=driver.find_element_by_css_selector("input[name='pc_name']").get_attribute('value')
ps_name=driver.find_element_by_css_selector("input[name='ps_name']").get_attribute('value')
slno_inpart=driver.find_element_by_css_selector("input[name='slno_inpart']").get_attribute('value')
st_code=driver.find_element_by_css_selector("input[name='st_code']").get_attribute('value')
ps_lat_long=driver.find_element_by_css_selector("input[name='ps_lat_long']").get_attribute('value')
part_no=driver.find_element_by_css_selector("input[name='part_no']").get_attribute('value')
part_name=driver.find_element_by_css_selector("input[name='part_name']").get_attribute('value')

record.append((c_id,epic_no,name,gender,age,rln_name,last_update,state,district,ac_name,ac_no,pc_name,ps_name,slno_inpart,st_code,ps_lat_long,part_no,part_name))

import pandas as pd
df=pd.DataFrame(record, columns=['c_id','epic_no','name','gender','age','rln_name','last_update','state','district','ac_name','ac_no','pc_name','ps_name','slno_inpart','st_code','ps_lat_long','part_no','part_name'])
df.to_csv('Voter.csv',index=False,encoding='utf-8')

#stop scraping
driver.quit()