import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
import time

def get_top(num):
    PATH = "C:\\Users\\vince\\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    #chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(PATH), chrome_options=chrome_options)
    driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F553266151399305")
    action = webdriver.ActionChains(driver)

    driver.implicitly_wait(1)
    load_dotenv()
    driver.find_element(By.ID, "email").send_keys(os.getenv('email'))
    driver.find_element(By.ID, "pass").send_keys(os.getenv('pass'))
    driver.find_element(By.ID, "loginbutton").click()

    listOfLinks = []
    listOfItems = []

    while len(listOfLinks) < num:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        listings = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@CLASS = 'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")))

        for list in listings:
            if len(listOfLinks) < num and len(listOfItems) < num:
                try:
                    second = list.find_element(By.XPATH, ".//span[contains(@CLASS, 'x4k7w5x x1h91t0o')]/a")
                    action.move_to_element(second)
                    action.perform()
                    link = second.get_attribute('href').split('?')[0]
                    if link not in listOfLinks:
                        listOfLinks.append(link)

                    item = list.find_element(By.XPATH, ".//span[contains(@CLASS, 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 x1j85h84')]/div").text
                    if item not in listOfItems:
                        listOfItems.append(item)  
                except:
                    pass
            else:
                break

    return listOfLinks, listOfItems


def get_recent(num):
    PATH = "C:\\Users\\vince\\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    #chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(PATH), chrome_options=chrome_options)
    driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F553266151399305%3Fsorting_setting%3DCHRONOLOGICAL_LISTINGS")
    action = webdriver.ActionChains(driver)
    driver.implicitly_wait(1)

    

    load_dotenv()
    driver.find_element(By.ID, "email").send_keys(os.getenv('email'))
    driver.find_element(By.ID, "pass").send_keys(os.getenv('pass'))
    driver.find_element(By.ID, "loginbutton").click()

    listOfLinks = []
    listOfItems = []

    while len(listOfLinks) < num:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        listings = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@CLASS = 'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")))

        for list in listings:
            if len(listOfLinks) < num and len(listOfItems) < num:
                try:
                    second = list.find_element(By.XPATH, ".//span[contains(@CLASS, 'x4k7w5x x1h91t0o')]/a")
                    action.move_to_element(second)
                    action.perform()
                    link = second.get_attribute('href').split('?')[0]
                    if link not in listOfLinks:
                        listOfLinks.append(link)

                    item = list.find_element(By.XPATH, ".//span[contains(@CLASS, 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 x1j85h84')]/div").text
                    if item not in listOfItems:
                        listOfItems.append(item)  
                except:
                    pass
            else:
                break

    return listOfLinks, listOfItems
                
    
         
           


        


