from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from selenium.webdriver.support.wait import WebDriverWait

from datetime import datetime
import pandas as pd
import numpy as np
import random
import time
import os
import re

now = datetime.now()
start_date = now.strftime('%d%m%Y')
os.makedirs('data/' + start_date , exist_ok=True)
keywords = [
    'data science'
]
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.jobstreet.com.my/')
driver.find_element(By.NAME, 'key').send_keys(keywords)
driver.find_element(By.XPATH, '//div/button[@data-automation="searchSubmitButton"]').send_keys(Keys.ENTER)
driver.implicitly_wait(3)

page = 1

while True:

    job_post_index = 0

    try:

        print(f'Collecting data: {page}....', end="")

        articles = driver.find_elements(By.TAG_NAME, "article")

        time.sleep(1 + 2*random.random())
        to_frame = []
        items = 0

        for article in articles:
        
            time.sleep(1 + 2*random.random())

            job_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(article))

            try:

                driver.execute_script('arguments[0].click();', job_button)
                items += 1

                try:
                    summary = driver.find_element(By.XPATH, "//div[@data-automation='jobDescription']").text.strip()

                except:
                    summary = None
                
            except:
                print(f'click {job_post_index} failed')

            location = article.find_elements(By.TAG_NAME, 'span')[3].text.strip()
            title = article.find_elements(By.TAG_NAME, 'span')[0].text.strip()
            company = article.find_elements(By.TAG_NAME, "span")[1].text.strip()

            test_salary = article.find_elements(By.TAG_NAME, "span")[5].text.strip()

            if re.search('myr', test_salary.lower()):
                salary = test_salary
            else:
                salary = None

            # try to get url,
            job_url = article.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
         
            job_info = {
                'location': location,
                'title': title,
                'company': company,
                'salary': salary,
                'summary': summary,
                'job_url': job_url}

            to_frame.append(job_info)
            job_post_index += 1
        
        framed_df = pd.DataFrame(to_frame)
        framed_df.to_csv('data/' + start_date + '/page' + str(page) + '.csv', index=False)
        print('Saved!')

        start_url = driver.current_url

        next_page = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,
                "//span[normalize-space()='Next']"
                )))

        driver.execute_script("arguments[0].click();", next_page)

        next_url = driver.current_url

        if start_url == next_url:
            print(f"Scraper stopped moving, scaping ended at page {page - 1}")
            break

        page += 1

    except:
        print(f"Exception hit, scaping ended at page {page - 1}")
        break

print('/nScrape End')




file_count = len(os.listdir("./data/" + start_date ))

result_df = pd.read_csv('jobstreet/' + start_date +'/page1.csv')

for page in range(2,file_count,1):

    print(f"loading page {page}....", end="")

    df_to_add = pd.read_csv('data/' + start_date + '/page'+ str(page) + '.csv')

    result_df = pd.concat([result_df, df_to_add])

    print('Done!')

# create the directory if it doesn't exist
directory = 'data/raw_' + start_date
if not os.path.exists(directory):
    os.makedirs(directory)

# save the file in the directory
result_df.to_csv(directory + '/page' + str(page) + '.csv', index=False)

result_df.shape