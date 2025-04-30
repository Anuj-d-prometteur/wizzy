
from logging import exception
from operator import is_not
from time import sleep
from turtledemo.clock import setup
import traceback
from warnings import catch_warnings
from weakref import finalize

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from Modules.Admin_Panel import Setup
from selenium.webdriver.common.action_chains import ActionChains


def Create_Guide(data,driver):
    print("Create Guide")
    try:
        driver.find_element(By.XPATH,"//div//a[@href='/guide']").click()
        header=driver.find_element(By.XPATH,"//div/header//b").text
        if header!="Guide":
            raise Exception(f"Unexpected header: Expected 'Guide', but got '{header}'")
        else:
            sleep(2)
            driver.find_element(By.XPATH,"//button[contains(text(),'Add New Guide')]").click()
            sleep(1)
            driver.find_element(By.XPATH,"(//input[@name='title'])[1]").send_keys(data[0])
            driver.find_element(By.XPATH,"//select[@name='difficulty_level']").click()
            sleep(1)
            driver.find_element(By.XPATH, f"//select[@name='difficulty_level']/option[@id='{data[1]}']").click()
            sleep(2)
            driver.find_element(By.XPATH,"//input[@name='earning_amount']").send_keys(data[2])
            driver.find_element(By.XPATH,"//input[@name='reading_duration']").send_keys(data[3])
            sleep(1)
            driver.find_element(By.XPATH,f"//select[@name='bookmaker']/option[@aria-labelledby='{data[4]}']").click()
            driver.find_element(By.XPATH,f"//select[@name='betting_exchange']/option[@aria-labelledby='{data[5]}']").click()
            sleep(1)
            driver.find_element(By.XPATH,"//input[@name='position']").send_keys(data[6])
            driver.execute_script("window.scrollBy(0, 500);")
        print("Filed Guide Data")

    except  Exception as e:
        print("closed exception ",{e})
        traceback.print_exc()


def Create_Dynamic_level(data,driver):
    try:
        sleep(1)
        driver.execute_script("window.scrollBy(0, 500);")
        driver.find_element(By.XPATH,"//input[@name='name']").send_keys(data[0])
        driver.find_element(By.XPATH,"//input[@name='level_number']").send_keys(data[1])
        driver.find_element(By.XPATH,"(//input[@name='title'])[2]").send_keys(data[2])
        sleep(1)
        driver.find_element(By.XPATH,"//input[@name='heading']").send_keys(data[3])
        driver.find_element(By.XPATH,"//input[@name='subheading']").send_keys(data[4])
        driver.execute_script("window.scrollBy(0, 400);")
        sleep(2)
        try:
            file_input = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")  # Adjust the XPath if necessary
            file_path = r"C:\Users\anujd\Downloads\2849-163375551_tiny.mp4"  # Replace with the actual file path
            file_input.send_keys(file_path)
        except Exception as b:
            traceback.print_exc()
            print("video Uploading fail!")
        sleep(2)
        driver.execute_script("window.scrollBy(0, 300);")
        driver.find_element(By.XPATH,"//input[@name='total_time']").send_keys("00:10:00")
        driver.find_element(By.XPATH,"//textarea[@name='transcription']").send_keys(data[5])
        sleep(1)
        print("Level Created Successfully!")

    except Exception as e:
        print("closed exception :", {e})
        traceback.print_exc()

def Guidebook(data,driver):
    try:
        sleep(3)
        driver.execute_script("window.scrollBy(0, 500);")
        driver.find_element(By.XPATH,"//select[@class='form-select w-auto']").click()
        sleep(1)
        DropDown=driver.find_element(By.XPATH, f"//div[@class='card-body']//select[@class='form-select w-auto']/option[@value='{data[1]}']")
        DropDown.click()
        sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Add Component')]").click()
        if data[0]=="text":
            driver.execute_script("window.scrollBy(0, 200);")
            textbox=driver.find_element(By.XPATH,"//div[@class='ql-editor ql-blank']")
            sleep(2)
            textbox.click()
            textbox.send_keys(data[2])
            print()
        elif data[0] == "Odds wizzer":
            DropDown.click()
            driver.find_element(By.XPATH, "//select[@class='form-select mt-2']")
            sleep(2)
            if data[1] == "Qualified Bet":
                driver.find_element(By.XPATH,
                                    "//select[@class='form-select mt-2']/option[@value='qualifiedBet']").click()
            else:
                driver.find_element(By.XPATH, "//select[@class='form-select mt-2']/option[@value='freeBe']").click()

            print()
        elif data[0]=="Open Account":
            DropDown.click()
            driver.find_element(By.XPATH,"").click()

        sleep(1)
        create_button = driver.find_element(By.XPATH, "//button[contains(text(),'Create Guide')]")
        actions = ActionChains(driver)
        #actions.move_to_element(element).perform()
        actions.scroll_to_element(create_button).perform()
        create_button.click()


    except Exception as e:
        print("Error is displayed: test case failed.")
        traceback.print_exc()

