import re
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("chromedriver")  

driver = webdriver.Chrome()

url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31"
driver.get(url)

time.sleep(3)
wait = WebDriverWait(driver, 10)

click_count = 0
previous_count = 0

while True:
    try:
        load_more_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='ipc-see-more__text']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(2)
        
        titles = driver.find_elements(By.CSS_SELECTOR, "h3[class='ipc-title__text']")
        if len(titles) == previous_count:
            print("No new content loaded. Stopping clicks.")
            break
        previous_count = len(titles)

        click_count += 1
        print(f"Clicked {click_count} times")
    except Exception as e:
        print("No more 'Load More' button found or all pages loaded.")
        break

titles = driver.find_elements(By.CSS_SELECTOR, "h3[class='ipc-title__text']")
movie_titles = [re.sub(r'^\d+\.\s*', '', title.text) for title in titles]

descriptions = driver.find_elements(By.XPATH, "//div[@class='sc-d49a611d-1 csbzhP']")
movie_descriptions = [description.text for description in descriptions]

min_length = min(len(movie_titles), len(movie_descriptions))
movie_titles = movie_titles[:min_length]
movie_descriptions = movie_descriptions[:min_length]

csv_filename = "scraped_2024.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Description"])
    writer.writerows(zip(movie_titles, movie_descriptions))

print(f"Data saved successfully in {csv_filename}")

driver.quit()
