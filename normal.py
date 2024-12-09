import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class A:
    def mine(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://soulunileaders.com/")
        print(driver.title)
        time.sleep(5)
        about_us_button = driver.find_element(By.XPATH,"//a[contains(@class,'drop-down')][normalize-space()='About Us']")
        about_us_button.click()
        time.sleep(5)
        print(driver.title)
        # login_button = driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
        # time.sleep(5)
        # print(driver.title)
        # user_name = driver.find_element(By.XPATH,"//input[@id='login_email']").send_keys("chinmaya.nayak@soulunileaders.com")
        # time.sleep(5)
        # password = driver.find_element(By.XPATH,"//input[@id='login_password']").send_keys("gayatri@1999")
        # time.sleep(5)
        # login = driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        # time.sleep(5)
        # career_footer = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//a[@class='career-footer']")))
        # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", career_footer)
        # time.sleep(5)
        # email = driver.find_element(By.XPATH,"//input[@id='login_email']").send_keys("chinmaya.nayak@soulunileaders.com")
        # time.sleep(5)
        # password = driver.find_element(By.XPATH,"//input[@id='login_password']").send_keys("gayatri@1999")
        # time.sleep(5)
        # login = driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        # time.sleep(5)
        # print(driver.title)
        driver.quit()

a = A()
a.mine()

