from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


def create_new_review(data,driver):
    try:
        print("Starting: Create Review")

        # Step 1: Navigate to Review Management
        driver.find_element(By.XPATH, '//*[@id="aside-dashboard"]/li[9]/a/span/span').click()
        sleep(2)
        header = driver.find_element(By.XPATH, '//*[@id="aside-dashboard"]/li[9]/a/span/span').text
        if header != "Review Management":
            print(f"Header mismatch. Expected: 'Review Management', Got: '{header}'")
            return

        # Step 2: Click "Add Review"
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/main/div/div[1]/div[2]/div/button').click()
        sleep(2)

        # Step 3: Upload image (optional)
        try:
            file_path = r"C:\Users\AjayRojekar\Pictures\Screenshots\Screenshot 2025-05-02 132747.png"  # Replace with your actual image path
            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
            driver.execute_script("window.scrollBy(0, 76);")
        except Exception as upload_err:
            print("Image upload skipped or failed:", upload_err)

        # Step 4: Fill form fields
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[2]/div[1]/input').send_keys(data[2])
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys(data[3])
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[3]/div[1]/input').send_keys(data[4])

        # Status dropdown
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[3]/div[2]/select'))
        sleep(1)
        dropdown.select_by_visible_text(data[1])

        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[4]/div/input').send_keys(data[5])
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[5]/div/textarea').send_keys(data[6])

        # Step 5: Click Save
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[6]/button').click()
        sleep(3)

        # Step 6: Validation
        if data[2] == "" or data[4] == "" or data[6] == "":
            if data[2] == "":
                first_name_err = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[1]").text
                print(f"First Name Error: {first_name_err}")
            if data[4] == "":
                username_err = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[2]").text
                print(f"Username Error: {username_err}")
            if data[6] == "":
                review_err = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[3]").text
                print(f"Review Error: {review_err}")
            driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
        else:
            success_msg = driver.find_element(By.XPATH, "//div[contains(text(),'Review created successfully.')]").text
            print(f"Success! Expected: '{data[7]}', Actual: '{success_msg}'")

    except Exception as e:
        print("closed exception ", {e})
        traceback.print_exc()




def edit_review(Edit_data, driver):
    try:
        print("Starting: Edit Review")

        # Step 1: Navigate to Review Management
        driver.find_element(By.XPATH, '//*[@id="aside-dashboard"]/li[9]/a/span/span').click()
        sleep(2)
        header = driver.find_element(By.XPATH, '//*[@id="aside-dashboard"]/li[9]/a/span/span').text
        if header != "Review Management":
            print(f"Header mismatch. Expected: 'Review Management', Got: '{header}'")
            return

        # Step 2: Click edit icon (assumed to be the first one)
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/main/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/div/button[2]').click()
        sleep(2)

        # # Optional: Delete old image and upload new image if path is provided
        # try:
        #     driver.find_element(By.XPATH, "//button[contains(text(),'Delete Image')]").click()
        #     sleep(1)
        #     file_path = r"C:\Users\AjayRojekar\Downloads\cracked-basketball-club-logo-vector-44927542.avif"  # Replace with your actual image path
        #     driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
        #     driver.execute_script("window.scrollBy(0, 76);")
        # except Exception as upload_err:
        #     print("Image upload skipped or failed:", upload_err)

        # Step 3: Edit fields
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[2]/div[1]/input').clear()
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[2]/div[1]/input').send_keys(Edit_data[2])  # First Name

        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[2]/div[2]/input').clear()
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys(Edit_data[3])  # Last Name

        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[3]/div[1]/input').clear()
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[3]/div[1]/input').send_keys(Edit_data[4])  # Username

        # Status Dropdown
        dropdown = Select(driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[3]/div[2]/select'))
        dropdown.select_by_visible_text(Edit_data[1])

        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[4]/div/input').clear()
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[4]/div/input').send_keys(Edit_data[5])  # Position

        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[5]/div/textarea').clear()
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[5]/div/textarea').send_keys(Edit_data[6])  # Review

        # Step 4: Save the updated review
        driver.find_element(By.XPATH, '//*[@id="portal-root"]/div[1]/div/div/div[2]/div[6]/button').click()
        sleep(3)

        # Step 5: Validation
        if Edit_data[2] == "" or Edit_data[4] == "" or Edit_data[6] == "":
            if Edit_data[2] == "":
                first_name_err = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[1]").text
                print(f"First Name Error: {first_name_err}")
            if Edit_data[4] == "":
                username_err = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[2]").text
                print(f"Username Error: {username_err}")
            if Edit_data[6] == "":
                review_err = driver.find_element(By.XPATH, "(//div[@class='w-100']//span)[3]").text
                print(f"Review Error: {review_err}")
            driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
        else:

            try:
                success_msg_element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Review updated successfully')]"))
                )
                print(f"Success message appeared: '{success_msg_element.text}'")
            except TimeoutException:
                print("Toast message not found within 10 seconds.")

    except Exception as e:
        print("Exception occurred while editing review:", e)
        traceback.print_exc()

def delete_review(driver):
    try:
        print("Starting: Delete Review")

        # Step 1: Navigate to Review Management
        driver.find_element(By.XPATH, '//*[@id="aside-dashboard"]/li[9]/a/span/span').click()
        sleep(2)
        header = driver.find_element(By.XPATH, '//*[@id="aside-dashboard"]/li[9]/a/span/span').text
        if header != "Review Management":
            print(f"Header mismatch. Expected: 'Review Management', Got: '{header}'")
            return

        # Step 2: Click delete icon (assumed to be the first one in the list)
        delete_btn_xpath = '//*[@id="root"]/div[1]/div/main/div/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/div/button[3]'
        driver.find_element(By.XPATH, delete_btn_xpath).click()
        sleep(1)

        # Step 3: Confirm deletion
        confirm_yes_xpath = '//button[contains(text(),"Yes")]'
        driver.find_element(By.XPATH, confirm_yes_xpath).click()
        sleep(2)

        # Step 4: Wait for success toast message
        try:
            success_msg_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,"//*[contains(text(), 'Review deleted successfully')]"))
            )
            print(f"Success message appeared: '{success_msg_element.text}'")
        except TimeoutException:
            print("message not found within 10 seconds after deletion.")

    except Exception as e:
        print("Exception occurred while deleting review:", e)
        traceback.print_exc()