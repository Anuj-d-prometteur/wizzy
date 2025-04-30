from logging import exception
from time import sleep
from turtledemo.clock import setup
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from Modules.Admin_Panel import Setup


def __init_():
    print()


class FAQ:

    def create_FAQ(self,data, driver):
        try:
            print("Enter FAQ Section")
            operation = data[3]

            driver.find_element(By.XPATH, "//a[@href='/faq']").click()

            header = driver.find_element(By.XPATH, "//div[@class='header-left col-md']/b").text
            print(header)

            if header != "Faq":
                exception(f"This is not a Faq window : {header}")
            else:
                if operation == "New":
                    sleep(1)
                    driver.find_element(By.XPATH, "//button[contains(text(),' Add New FAQ')]").click()
                    sleep(2)
                    driver.find_element(By.XPATH, "//input[@name='question']").send_keys(data[0])
                    driver.find_element(By.XPATH, "//input[@name='position']").send_keys('8')
                    driver.find_element(By.XPATH, "//textarea[@class='form-control']").send_keys(data[1])
                    sleep(3)
                    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
                    sleep(2)
                    error_msg = driver.find_element(By.XPATH, "//div[@role='alert']/div[2]").text
                    if error_msg != data[2]:
                        exception(f"Test Case Filed, Actual Message:{error_msg} and Expected Message : {data[2]}")
                    else:
                        print("Test Case Pass")
                else:
                    sleep(2)
                    driver.find_element(By.XPATH, "//button[contains(text(),' Add New FAQ')]").click()
                    if operation == "Question":
                        driver.find_element(By.XPATH, "//input[@name='question']").clear()
                        driver.find_element(By.XPATH, "//input[@name='question']").send_keys(data[0])
                    else:
                        driver.find_element(By.XPATH, "//textarea[@class='form-control']").clear()
                        driver.find_element(By.XPATH, "//textarea[@class='form-control']").send_keys(data[0])
                    sleep(2)
                    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
                    error_msg = driver.find_element(By.XPATH, "//div[@role='alert']/div[2]").text
                    e=""
                    if error_msg != data[2]:
                        e=error_msg
                        exception(f"Test Case Filed, Actual Message:{error_msg} and Expected Message : {data[2]}")
                    else:
                        print("Test Case Pass")
                    return e
        except Exception as e:
            exception(f"Test Case Filed, Actual Message:{e} and Expected Message : {data[2]}")
            traceback.print_exc()



    def edit_Faq(self,data, driver):
        try:
            driver.find_element(By.XPATH, "//a[@href='/faq']").click()
            header = driver.find_element(By.XPATH, "//div[@class='header-left col-md']/b").text
            if header != "Faq":
                exception(f"This is not a Faq window : {header}")
            else:
                sleep(2)
                if process == "Question":
                    sleep(2)
                    driver.find_element(By.XPATH, "//input[@name='question']").send_keys(data[0])
                    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
                    sleep(2)
                    error_msg = driver.find_element(By.XPATH, "//div[@role='alert']/div[2]").text
                    if error_msg != data[2]:
                        exception(f"Test Case Filed, Actual Message:{error_msg} and Expected Message : {data[2]}")
                    else:
                        print("Test Case Pass")
                elif process== "Position":
                    sleep(2)
                    text=int(driver.find_element(By.XPATH,"//input[@name='position']").get_attribute('value'))
                    sleep(2)
                    driver.find_element(By.XPATH, "//input[@name='position']").send_keys(data[0])
                    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
                    sleep(2)
                    error_msg = driver.find_element(By.XPATH, "//div[@role='alert']/div[2]").text
                    if error_msg != data[2]:
                        exception(f"Test Case Filed, Actual Message:{error_msg} and Expected Message : {data[2]}")
                    else:
                        print("Test Case Pass")
                elif process =="Answer":
                    sleep(2)
                    driver.find_element(By.XPATH, "//textarea[@name='answer']").send_keys(data[0])
                    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
                    sleep(2)
                    error_msg = driver.find_element(By.XPATH, "//div[@role='alert']/div[2]").text
                    if error_msg != data[2]:
                        exception(f"Test Case Filed, Actual Message:{error_msg} and Expected Message : {data[2]}")
                    else:
                        print("Test Case Pass")
                else:
                    sleep(2)
                    driver.find_element(By.XPATH, "//input[@name='question']").send_keys(data[0])
                    driver.find_element(By.XPATH, "//input[@name='position']").send_keys(data[0])
                    driver.find_element(By.XPATH, "//textarea[@name='answer']").send_keys(data[0])
                    sleep(2)
                    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
                    error_msg = driver.find_element(By.XPATH, "//div[@role='alert']/div[2]").text
                    if error_msg != data[2]:
                        exception(f"Test Case Filed, Actual Message:{error_msg} and Expected Message : {data[2]}")
                    else:
                        print("Test Case Pass")
        except Exception as e:
            print("Test case Failed")
            traceback.print_exc()



    def delete_FAQ(self,data, driver):
        try:
            driver.find_element(By.XPATH, "//a[@href='/faq']").click()
            header = driver.find_element(By.XPATH, "//div[@class='header-left col-md']/b").text

            if header != "Faq":
                exception(f"This is not a Faq window : {header}")
            else:
                driver.find_element(By.ID, "searchInput").send_keys(data[0])
                sleep(2)
                driver.find_element(By.XPATH, "//table//tr[1]//td[4]//button[3]").click()
                sleep(1)
                driver.find_element(By.XPATH, "//button[contains(text(),'Yes')]").click()
                sleep(1)
                error = driver.find_element(By.XPATH, "(//div[@role='alert']//div)[2]").text
                if error != data[3]:
                    exception(f"Expected:- {data[1]} , Actual:- {error}")
                else:
                    print("Test Case Pass!")
                print()

        except Exception as e:
            print("")


