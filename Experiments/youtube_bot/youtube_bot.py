from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time


# number_of_drivers = int(input("Enter the number of drivers : " ))
# time_to_refresh = int(input("Enter refresh rate time in seconds : " ))
# url = input("Enter URL: ")
number_of_drivers = 5
time_to_refresh = 60
url = "https://www.youtube.com/watch?v=OhLE_s5YuwU"
drivers = []

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options))
    drivers[i].get(url)

while True:
    time.sleep(time_to_refresh)
    for i in range(number_of_drivers):
        drivers[i].refresh()