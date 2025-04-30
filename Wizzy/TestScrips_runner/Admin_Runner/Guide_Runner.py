
from Modules.Admin_Panel import Guide
from Modules.Admin_Panel import Setup

Guide_data=["test","easy",3900,"00:10:30","flashscore","flashscore_12",10]
level_data=["introduction",1,"Introduction","Heading","flashscore","flashscore_12"]
data=["text","text","Sports betting is the activity of predicting sports results and placing a wager on the outcome. Usually, the wager is in the form of money."]
def test_create_guide():
    driver = Setup.login_adminAccount()
    print("enter method")
    Guide.Create_Guide(Guide_data,driver)
    Guide.Create_Dynamic_level(level_data,driver)
    Guide.Guidebook(data,driver)
    Setup.logout_adminaccount(driver)



