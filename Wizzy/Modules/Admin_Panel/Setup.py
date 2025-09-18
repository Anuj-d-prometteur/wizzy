
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
import traceback



def login_useraccount():
    try:
        service = Service(r"C:\Users\Anuj d\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://wizzy-admin.vercel.app/auth-pages/login")
        driver.maximize_window()
        print("inter in code")
        sleep(2)
        driver.find_element(By.XPATH,"//input[@id=':r0:']").send_keys("anujsubcription2@yopmail.com")
        driver.find_element(By.XPATH,"//input[@id=':r1:']").send_keys("Pass@123")
        sleep(3)
        driver.find_element(By.XPATH,"//button[contains(text(),'Sign In')]").click()
        print("wait for a min")
        sleep(10)
        username = driver.find_element(By.XPATH, "(//button[@type='button']/div/span)[3]").text
        if username== "Wizzy_QA Tester":
            print("Test case pass")
        else:
            print("expected : 'Wizzy_QA Tester' , Actual : {}".format(username))
        e=""
        return e

    except Exception as e:
        print("closed exception ",{e})
        traceback.print_exc()


def logout_userAccount(driver):
    try:
        sleep(3)
        driver.find_element(By.XPATH,"(//button[@type='button'])[2]").click()
        sleep(1)
        driver.find_element(By.XPATH,"//div[@id='dropdown-user']//li/button").click()
        sleep(1)
        driver.find_element(By.XPATH,"//div[2]/div[1]//div[2]/button[2]").click()
        sleep(2)

    except Exception as e:
        print({e})
        traceback.print_exc()


def login_adminAccount():
    try:
        #service = Service(EdgeChromiumDriverManager().install())
        service = Service(r"C:\Users\Anuj d\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://wizzy-admin.vercel.app/auth-pages/login")
        driver.maximize_window()
        print("Script executed successfully")
        driver.find_element(By.XPATH,"//input[@id='loginUsername']").send_keys("wizzyadmin@yopmail.com")
        driver.find_element(By.XPATH,"//input[@id='loginPassword']").send_keys("Pass@123")
        sleep(5)
        driver.execute_script("window.scrollBy(0, 900);")
        driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
        print("wait for a min")
        sleep(4)
        login_toster = driver.find_element(By.XPATH, "//div[@class='header-left col-md']/b").text
        print(login_toster)
        if login_toster== "Dashboard":
            print("Test case pass")
        else:
            print("expected : 'Login successful' , Actual : {}".format(login_toster))
        e=""
        return driver
    except Exception as e:
        print("closed exception ",{e})
        traceback.print_exc()


def logout_adminaccount(driver):
    try:
        sleep(3)
        driver.find_element(By.XPATH,"//button[@type='button']//b[contains(text(),'Logout')]").click()
        sleep(3)
        driver.find_element(By.XPATH,"//div[2]/div[1]//div[2]/button[2]").click()
        sleep(2)
        logout_toster= driver.find_element(By.XPATH,"//div[@role='alert']/div[2]").text
        if logout_toster== "Logout Successfully":
            print("Test case pass")
        else:
            print("expected : 'Logout Successfully' , Actual : {}".format(logout_toster))
        e=""
        driver.close()
        return e

    except Exception as e:
        print("Error: ",{e})
        traceback.print_exc()

