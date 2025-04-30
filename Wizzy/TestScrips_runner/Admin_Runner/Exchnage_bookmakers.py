from logging import exception
from time import sleep
from turtledemo.clock import setup
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service













def create_Exchange_bookmakers(data,driver):
     try:
         print("inter the method")
         driver.find_element(By.XPATH,"//div[@class='aside-body']//a[@href='/bookmakers-Management']").click()
         headers=driver.find_element(By.XPATH,"//b[contains(text(),'Bookmakers Management')]").text
         if headers!="Bookmakers Management":
             print("Expected Name: 'Bookmakers Management' , Actual :",headers )
         else:
             if "Bookmakers"!=data[5]:
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
             driver.find_element(By.XPATH,"//input[@name='title']").send_keys(data[1])
             driver.find_element(By.XPATH,"//input[@name='url']").send_keys(data[2])
             driver.find_element(By.XPATH,"//select[@name='status']").click()
             driver.find_element(By.XPATH,f"//select[@name='status']/option[@value='{data[0]}']").click()
             driver.find_element(By.XPATH,"//button[contains(text(),'Save')]").click()
         sleep(3)
         if data[1]=="" or data[2]=="":
             title_ui_msg=""
             url_ui_msg=""
             if data[1]=="" and data[2]!="":
                 sleep(1)
                 title_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[1]").text
             elif data[2]=="" and data[1]!="":
                 sleep(1)
                 url_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[2]").text
             else:
                 sleep(1)
                 title_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[1]").text
                 url_ui_msg = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[2]").text
             sleep(2)
             driver.find_element(By.XPATH,"//div[@class='modal-content']//button[@aria-label='Close']").click()
             if data[1]=="" and data[2]!="":
                 if data[1]==title_ui_msg:
                     print(f"Test case pass!: Expected ='{data[4]}',Actual ='{title_ui_msg}'")
                 else:
                    print(f"Test result: Expected ='{data[4]}',Actual ='{title_ui_msg}'")
             elif data[2]=="" and data[1]!="":
                 if data[2]==url_ui_msg:
                     print(f"Test case pass!: Expected ='{data[3]}',Actual ='{url_ui_msg}'")
                 else:
                    print(f"Test result: Expected ='{data[3]}',Actual ='{url_ui_msg}'")
             else:
                 if data[3]==url_ui_msg and data[4]==title_ui_msg:
                     print(f"Test case pass!: Expected ='{data[3]}',Actual ='{url_ui_msg}'")
                     print(f"Test case pass!: Expected ='{data[4]}',Actual ='{title_ui_msg}'")
                 else :
                     print(f"Test Case Failed: Expected ='{data[3]}',Actual ='{url_ui_msg}'")
                     print(f"Test Case Failed: Expected ='{data[4]}',Actual ='{title_ui_msg}'")
         else:
             successfully_msg=driver.find_element(By.XPATH,"//div[contains(text(),'Bookmaker added successfully.')]").text
             print(f" Expected ='{data[3]}',Actual ='{successfully_msg}'")
             print("Test Case Pass!")
         e=None
         return e
     except Exception as e:
         print("closed exception ", {e})
         traceback.print_exc()