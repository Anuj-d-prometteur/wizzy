#from robot.libraries.DateTime import get_current_date
from datetime import timezone
from time import sleep
import pytest

from Modules.Admin_Panel import Bookmakers
from Modules.Admin_Panel import Setup


#validation meassage
#//div[contains(text(),'Bookmaker deleted successfully')]
url_msg="Url is required!"
Title_msg="Title is required!"
Successfully_message= "Bookmaker added successfully."
Updated_message="Bookmaker updated successfully"
Delete_message="Bookmaker deleted successfully"
Invalid_title_message="is not blank"
Invalid_URl_message=""

name=timezone
Title_name="wizzy_automation"+str(name)

Url_name="http://"+str(Title_name)+"/test.com"

data = ["Bookmakers","True", "wizzy", "http://wizzy12.com",Successfully_message]

data1 = ["Exchange Bookmakers","True","wizzy", "http://wizzy.com",Successfully_message]

data2 = ["Exchange Bookmakers","True", "wizzy", "http://wizzy.com",Successfully_message]

data3 = ["Exchange Bookmakers","True", "wizzy", "http://wizzy.com",Successfully_message]

data4 = ["Exchange Bookmakers","True", "wizzy", "http://wizzy.com",Successfully_message]

#<<<<<<<<<<   Test Cases    >>>>>>>>>
def __init__():
    print()
#verify the creation bookmakers
def test_create_bookmakers():
    driver=Setup.login_adminAccount()
    print("create bookmakers")

    Bookmakers.create_bookmakers(data,driver)
    print("logout driver")
    Setup.logout_adminaccount(driver)

def test_create_Exchange_bookmakers():
    driver=Setup.login_adminAccount()
    print("create Exchange bookmakers")
    Bookmakers.create_bookmakers(data1,driver)
    print("logout driver")
    Setup.logout_adminaccount(driver)

#verify the mandatory filed for create bookmakers
def test_create_bookmakers_Allmandatory_filed(driver):
    print("Start:- verify_create_bookmakers_Allmandatory_filed")
    data3 = ["True","", "",url_msg,Title_msg,"Bookmakers"]
    Bookmakers.create_bookmakers(data,driver)
    print("Closed:- verify_create_bookmakers_Allmandatory_filed")

def test_create_bookmakers_Titlemandatory_filed(driver):
    print("Start:- verify_create_bookmakers_Titlemandatory_filed")
    data = ["True","",Url_name,url_msg,Title_msg,"Bookmakers"]
    Bookmakers.create_bookmakers(data,driver)
    print("Closed:- verify_create_bookmakers_Titlemandatory_filed")


def test_create_bookmakers_URLmandatory_filed(driver):
    print("Start: verify_create_bookmakers_URLmandatory_filed")
    data = ["True",Title_name,"",url_msg,Title_msg,"Bookmakers"]
    Bookmakers.create_bookmakers(data,driver)
    print("Closed: verify_create_bookmakers_URLmandatory_filed")

#verify changing title and url of bookmakers
def test_Edit_Bookmakers():
    driver = Setup.login_adminAccount()
    print("create bookmakers")
    print(Title_name)
    data = ["True",Title_name[0], Url_name,Updated_message,"Edit_All_bookmakers"]
    Bookmakers.edit_bookmakers(data,driver)
    print("logout driver")
    Setup.logout_adminaccount(driver)

#verify the changing all bookmakers details
def test_Edit_statusOf_Bookmakers():
    driver = Setup.login_adminAccount()
    print("create bookmakers")
    print(Title_name)
    data = ["False",Title_name[0], Url_name,Updated_message,"Edit_All_bookmakers"]
    Bookmakers.edit_bookmakers(data,driver)
    print("logout driver")
    Setup.logout_adminaccount(driver)

#verify the changing status of bookmakers
def test_statusOf_Bookmakers():
    driver = Setup.login_adminAccount()
    print("Update bookmakers")
    print(Title_name)
    data = ["False",Title_name[0], Url_name,Updated_message,"Only_Status"]
    Bookmakers.edit_bookmakers(data,driver)
    print("logout driver")
    Setup.logout_adminaccount(driver)

def test_delete_bookmakers():
    driver = Setup.login_adminAccount()
    data = [Delete_message,"Soccer"]
    Bookmakers.Delete_bookmakers(data,driver)
    print("logout driver")
    Setup.logout_adminaccount(driver)


#verify_create_bookmakers()
# driver=Setup.login_adminAccount()
# verify_create_bookmakers_Allmandatory_filed(driver)
# sleep(4)
# verify_create_bookmakers_Titlemandatory_filed(driver)
# sleep(4)
# verify_create_bookmakers_URLmandatory_filed(driver)
# sleep(4)
# Setup.logout_adminaccount(driver)

#verify_Edit_Bookmakers()
#verify_statusOf_Bookmakers()
#verify_delete_bookmakers()
#verify_create_Exchange_bookmakers()
#print(data)


