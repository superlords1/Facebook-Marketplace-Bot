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

def getPosts(num):
    PATH = "C:\\Users\\vince\\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(PATH), chrome_options=chrome_options)
    driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F553266151399305")
    
    # log in
    driver.implicitly_wait(1)
    load_dotenv()
    driver.find_element(By.ID, "email").send_keys(os.getenv('email'))
    driver.find_element(By.ID, "pass").send_keys(os.getenv('pass'))
    driver.find_element(By.ID, "loginbutton").click()
    ListOfLinks = []
    ListOfTexts = []
    LinkCount, TextCount = 0, 0
    
    while LinkCount < num:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        listings = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@CLASS = 'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")))
        for list in listings:
            try:
                element = list.find_element(By.XPATH, ".//li[contains(@class, 'x1rg5ohu x1emribx x1i64zmx')]/a")
                comment_link = element.get_attribute('href')
                split = comment_link.split('?comment')
                link = split[0]
            except:
                pass
            try:
                if link not in ListOfLinks:
                    ListOfLinks.append(link)
                    ListOfTexts.append(list.text.split("Message")[0])
                    LinkCount += 1
                    if len(ListOfLinks) >= num:
                        #return [ListOfLinks, ListOfTexts]
                        break
                else:
                    pass
            except:
                pass
    '''       
    for i in range(LinkCount):
        print(ListOfLinks[i])
        print(ListOfTexts[i])
        print("----------------------------------------------------")
    '''
    return ListOfLinks, ListOfTexts
    
        
        


