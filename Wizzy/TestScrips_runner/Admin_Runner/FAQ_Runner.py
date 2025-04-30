#from robot.libraries.DateTime import get_current_date
from os import times
from time import timezone

from selenium.webdriver.common.devtools.v85.animation import get_current_time

from Modules.Admin_Panel import FAQ
from Modules.Admin_Panel import Setup
import pytest

date= timezone


Question="I purchase subscription on :"+str(date)
Ans="Thanks you for that, your next date is :"+str(date)

up_que=Question
up_Ans=Ans

success_meg="FAQ created successfully."
#success_meg="FAQ created successfu."
error_Que_msg="A FAQ with this question already exists."
error_Ans_msg="A FAQ with this answer already exists."
#error_Ans_msg="A FAQ with this answer already exists."
error_del_msg="FAQ deleted successfully."

data=[up_que,up_Ans,Question,Ans]
print(data)


def test_create_FAQ():
    operation= "New"
    driver= Setup.login_adminAccount()
    data=[Question,Ans,success_meg,operation]
    FAQ.create_FAQ(data,driver)
    Setup.logout_adminaccount(driver)

def test_create_Duplicate_Question_FAQ():
    driver= Setup.login_adminAccount()
    data=[up_que,up_Ans,error_Que_msg]
    FAQ.create_FAQ(data,driver)
    Setup.logout_adminaccount(driver)

def test_create_Duplicate_Ans_FAQ():
    driver= Setup.login_adminAccount()
    data=[up_que,up_Ans,error_Ans_msg]
    FAQ.create_FAQ(data,driver)
    Setup.logout_adminaccount(driver)

def test_Delete_FAQ():
    driver=Setup.login_adminAccount()
    data=[up_que,error_del_msg]
    FAQ.delete_FAQ(data,driver)
    Setup.logout_adminaccount(driver)

