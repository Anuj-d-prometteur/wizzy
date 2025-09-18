from datetime import timezone
import pytest
from time import sleep
from Modules.Admin_Panel import Reviews
from Modules.Admin_Panel import Setup

# Validation and success messages
URL_REQUIRED_MSG = "Url is required!"
TITLE_REQUIRED_MSG = "Title is required!"
SUCCESS_MSG = "Bookmaker added successfully."
UPDATED_MSG = "Bookmaker updated successfully"
DELETE_MSG = "Bookmaker deleted successfully"
INVALID_TITLE_MSG = "is not blank"
INVALID_URL_MSG = ""

# Dynamic test data
from datetime import datetime
name = datetime.now().strftime("%Y%m%d%H%M%S")
Title_name = f"wizzy_automation{name}"
Url_name = f"http://{Title_name}/test.com"

# Test data variations
data = ["","Active","tedstsa", "ussersa", "Aksaf", "982" , "Working","Review created successfully.",  SUCCESS_MSG]
Edit_data = ["","Active","eseae", "dsesaesr", "tesesasr", "269" , "Working","Review updated successfully",  SUCCESS_MSG]

#<<<<<<<<<<   Test Cases    >>>>>>>>>

def test_create_new_review():
    driver = Setup.login_adminAccount()
    print("Test: create_new_review")
    Reviews.create_new_review(data, driver)
    Setup.logout_adminaccount(driver)

def test_edit_review():
    driver = Setup.login_adminAccount()
    print("Test: edit_review")
    Reviews.edit_review(Edit_data, driver)
    Setup.logout_adminaccount(driver)

def test_delete_review():
    driver = Setup.login_adminAccount()
    print("Test: delete_review")
    Reviews.delete_review(driver)
    Setup.logout_adminaccount(driver)