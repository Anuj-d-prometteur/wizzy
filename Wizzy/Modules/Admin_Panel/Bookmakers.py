from logging import exception
from time import sleep
from turtledemo.clock import setup
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service



def create_bookmakers(data,driver):
     try:
         print("inter the method")
         driver.find_element(By.XPATH,"//div[@class='aside-body']//a[@href='/bookmakers-Management']").click()
         headers=driver.find_element(By.XPATH,"//b[contains(text(),'Bookmakers Management')]").text
         if headers!="Bookmakers Management":
             print("Expected Name: 'Bookmakers Management' , Actual :",headers )
         else:
             if "Bookmakers"!=data[0]:
                 driver.find_element(By.XPATH,"//div/span[contains(text(),'Exchange Bookmakers')]").click()
             sleep(2)
             driver.find_element(By.XPATH,"//button[@class='btn add-bookmakers']").click()
             sleep(2)
             try:
                 file_input = driver.find_element(By.XPATH,"//input[@name='file']")
                 #file_input.click()
                 file_path =r"C:\Users\anujd\Downloads\pngwing23.png"
                 file_input.send_keys(file_path)
                 mesg = driver.find_element(By.XPATH,"").text
                 b=mesg
                 if mesg != "":
                     exception("File Not Uploaded")
                 return b
             except Exception as b:
                 print("File Uploading fail! :-",b)
             driver.find_element(By.XPATH,"//input[@name='title']").send_keys(data[2])
             driver.find_element(By.XPATH,"//input[@name='url']").send_keys(data[3])
             driver.find_element(By.XPATH,"//select[@name='status']").click()
             driver.find_element(By.XPATH,f"//select[@name='status']/option[@value='{data[1]}']").click()
             driver.find_element(By.XPATH,"//button[contains(text(),'Save')]").click()
         sleep(3)
         if data[2]=="" or data[3]=="":
             title_ui_msg=""
             url_ui_msg=""
             if data[2]=="" and data[3]!="":
                 sleep(1)
                 title_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[1]").text
             elif data[3]=="" and data[2]!="":
                 sleep(1)
                 url_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[2]").text
             else:
                 sleep(1)
                 title_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[1]").text
                 url_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[2]").text
             sleep(2)
             driver.find_element(By.XPATH,"//div[@class='modal-content']//button[@aria-label='Close']").click()
             if data[2]=="" and data[3]!="":
                 if data[2]==title_ui_msg:
                     print(f"Test case pass!: Expected ='{data[5]}',Actual ='{title_ui_msg}'")
                 else:
                    print(f"Test result: Expected ='{data[5]}',Actual ='{title_ui_msg}'")
             elif data[3]=="" and data[2]!="":
                 if data[3]==url_ui_msg:
                     print(f"Test case pass!: Expected ='{data[4]}',Actual ='{url_ui_msg}'")
                 else:
                    print(f"Test result: Expected ='{data[4]}',Actual ='{url_ui_msg}'")
             else:
                 if data[4]==url_ui_msg and data[5]==title_ui_msg:
                     print(f"Test case pass!: Expected ='{data[4]}',Actual ='{url_ui_msg}'")
                     print(f"Test case pass!: Expected ='{data[5]}',Actual ='{title_ui_msg}'")
                 else :
                     print(f"Test Case Failed: Expected ='{data[4]}',Actual ='{url_ui_msg}'")
                     print(f"Test Case Failed: Expected ='{data[5]}',Actual ='{title_ui_msg}'")
         else:
             successfully_msg=driver.find_element(By.XPATH,"//div[contains(text(),'Bookmaker added successfully.')]").text
             print(f" Expected ='{data[4]}',Actual ='{successfully_msg}'")
             print("Test Case Pass!")
         e=None
         return e
     except Exception as e:
         print("closed exception ", {e})
         traceback.print_exc()

def edit_bookmakers(data,driver):
    try:
        Name=None
        Url=None
        print("Start Execution")
        driver.find_element(By.XPATH, "//div[@class='aside-body']//a[@href='/bookmakers-Management']").click()
        headers = driver.find_element(By.XPATH, "//b[contains(text(),'Bookmakers Management')]").text
        if headers != "Bookmakers Management":
            print("Expected Name: 'Bookmakers Management' , Actual :", headers)
        else:
            sleep(2)
            if data[4]!="Only_Status":
                driver.find_element(By.XPATH,"(//table//tr[1]/td[6]//button)[1]").click()
                sleep(1)
                driver.find_element(By.XPATH, "//input[@name='title']").clear()
                driver.find_element(By.XPATH, "//input[@name='title']").send_keys(data[1])
                driver.find_element(By.XPATH, "//input[@name='url']").clear()
                driver.find_element(By.XPATH, "//input[@name='url']").send_keys(data[2])
                driver.find_element(By.XPATH, "//select[@name='status']").click()
                sleep(1)
                driver.find_element(By.XPATH, f"//select[@name='status']/option[@value='{data[0]}']").click()
                driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
                error_msg = driver.find_element(By.XPATH,"//div[contains(text(),'Bookmaker updated successfully')]").text
                sleep(2)
                if error_msg != data[3]:
                    exception("successfully message is not displayed")
                    exit()
                else:
                    driver.find_element(By.XPATH, "//input[@id='searchInput']").clear()
                    driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys(data[1])
                    sleep(2)
                    Name = driver.find_element(By.XPATH, "//table//tr[1]/td[3]").text
                    Url = driver.find_element(By.XPATH, "//table//tr[1]/td[4]").text
                    sleep(1)
                sleep(3)
                if Name != data[1] and Url != data[2]:
                    exception("Updated Name and URl is not match")
                else:
                    print("Test cases pass")
            else:
                name = driver.find_element(By.XPATH, "//table//tr[1]/td[3]").text
                status=driver.find_element(By.XPATH,"//table//tr[1]/td[5]//button").text
                driver.find_element(By.XPATH, "//table//tr[1]/td[5]//button").click()
                sleep(2)
                if status=="Active":
                    driver.find_element(By.XPATH,"//table//tr[1]/td[5]//div[contains(text(),'InActive')]").click()
                else:
                    driver.find_element(By.XPATH, "//table//tr[1]/td[5]//li[1]/div").click()
                sleep(3)
                error_msg = driver.find_element(By.XPATH,"//div[contains(text(),'Bookmaker updated successfully')]").text
                if error_msg != data[3]:
                    exception("successfully message is not displayed")
                else:
                    driver.find_element(By.XPATH, "//input[@id='searchInput']").click()
                    driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys(name)
                    sleep(2)
                    up_status = driver.find_element(By.XPATH, "//table//tr[1]/td[5]//button").text
                    sleep(1)
                    if up_status==status:
                        exception("Status is not Updated")
                    else:
                        print("Test cases pass ")

    except Exception as e:
        print("closed exception ", {e})
        traceback.print_exc()


def Delete_bookmakers(data,driver):
    try:
        print("Start Execution")
        driver.find_element(By.XPATH, "//div[@class='aside-body']//a[@href='/bookmakers-Management']").click()
        headers = driver.find_element(By.XPATH, "//b[contains(text(),'Bookmakers Management')]").text
        if headers != "Bookmakers Management":
            print("Expected Name: 'Bookmakers Management' , Actual :", headers)
        else:
            sleep(3)
            #name = driver.find_element(By.XPATH, "//table//tr[1]/td[3]").text
            driver.find_element(By.XPATH, "//input[@id='searchInput']").clear()
            driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys(data[1])
            sleep(2)
            driver.find_element(By.XPATH,"(//table//tr[1]/td[6]//button)[2]").click()
            sleep(1)
            driver.find_element(By.XPATH,"//button[contains(text(),'Yes')]").click()
            sleep(2)
            error_msg = driver.find_element(By.XPATH, "//div[@role='alert']//div[contains(text(),'Bookmaker deleted successfully')]").text
            if error_msg != data[0]:
                exception("successfully message is not displayed")
            sleep(3)
            driver.find_element(By.XPATH, "//input[@id='searchInput']").clear()
            sleep(3)
            driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys(data[1])
            sleep(6)
            if len(driver.find_elements(By.XPATH,"//table//tr[1]/td"))==0:
                print("Test Case Passed: The Bookmakers was successfully deleted.")
            else:
                exception("Test Case Failed: The Bookmakers still exists after deletion.")
    except Exception as e:
        print("closed exception ", {e})
        traceback.print_exc()
