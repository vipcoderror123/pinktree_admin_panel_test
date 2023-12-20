import logging
import zipfile
from time import process_time
from time import sleep
import unittest

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGGER = logging.getLogger(_name_)

# to push local to remote repo
# git add .
# git commit -m "commit"
# git push

# to pull to local repo from remote repo
# git pull
# repository 


class PinktreeIntegrationTest():
    
    def setUp(self):
        try:
             chrome_options = Options()
             chrome_options.add_argument("enable-automation")

             chrome_options.add_argument("--no-sandbox")
             # chrome_options.add_experimental_option("useAutomationExtension", False)
             # chrome_options.add_argument("--incognito")
             # Fix for cannot get automation extension

             chrome_options.add_argument("--start-maximized")
             chrome_options.add_argument("--disable-dev-shm-usage")

             chrome_options.add_argument(
             "user-data-dir=C:\\Users\\sankr\\Downloads\\Documents\\Documents\\Temp_profile"
             #"user-data-dir=/Users/akshayvishwakarma/Documents/Vipul_Jurel/temp"
             )


             # chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})

            
             self.driver = webdriver.Chrome(options=chrome_options)
             driver = self.driver
             driver.set_page_load_timeout(60)
             driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled": False})
             driver.get("http://69.49.231.128:7575")
             self.login_flow()
        except:
             pass

    def login_flow(self):
        LOGGER.warning("-------Inside Login Flow-------")
        # warning
        # error
        # info
        # critical
        # debug
        
        while True:
            try:
                
                driver = self.driver
                sleep(5)

                # ---------- Check username and password validation ----------
                self._testLoginPasswordValidation(driver)
                # ---------- End of username and password validation ----------

                driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("8888888888")
                driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("123123")
                driver.find_element(By.XPATH, '//*[@id="login_btn"]').click()

                LOGGER.warning("-------Existing Login Flow-------")
                print("\n\n\n")
                sleep(5)
                self.user_flow()
                sleep(2)
                self.goal_flow()
                # self.activity_flow()
                # self.symptoms_flow()
                sleep(5)
                self.tearDown()
                break
            except:
                    
                LOGGER.warning("Element not found. Waiting for 5 sec...")
                sleep(5)
                pass

    def _testLoginPasswordValidation(self, driver):
        driver.find_element(By.XPATH, '//*[@id="login_btn"]').click()
           
        getErrorMsg = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '#toast-container > div > .toast-message'))).text
                        #name-error
                
        if getErrorMsg.strip() == "Please enter Phone Number":
            LOGGER.warning("Phone Number and Password Validation Passed")
        else:
            LOGGER.warning("Validation Error")
            return


    def user_flow(self):
        LOGGER.warning("-------------User Tab Testing  Started---------------")
        driver = self.driver
        while True:
            try:
                # login
                driver.find_element(
                    By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/a'
                ).click()
                
                sleep(2)
                
                driver.find_element(
                    By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[1]/a'
                ).click()
                
                break
            except:
                sleep(5)
                pass
            
            # 21 Nov
            # first task : fill all form in user then click on create
        while True:
            try:
                sleep(2)
                driver.find_element(By.XPATH, '//*[@id="create_user_btn"]').click()
                sleep(2)
                # validation 
                user_name = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
                       (By.CSS_SELECTOR, '#name-error'))).text
                self.validate_field(user_name, "Please enter Name", "Name Field Validation Passed")
                
                # mobile number
                mobile_num = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
                       (By.CSS_SELECTOR, '#mobile_number-error'))).text          
                self.validate_field(mobile_num, "Please enter Mobile Number", "Mobile Field Validation Passed")
                
                # email
                user_mail= WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
                       (By.CSS_SELECTOR, '#email-error'))).text           
                self.validate_field(user_mail, "Please enter Email", "Mail Field Validation Passed")
                
                #password
                user_password = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
                       (By.CSS_SELECTOR, '#password-error'))).text
                self.validate_field(user_password, "Please enter Password", "Password Field Validation Passed")
                # Task  1 . add parameter named validation error where you can add own eroor text
                
                # validation end
                # create validation started

                test_input = {
                "name" : "Sanskruti",
                "email" : "sanskruti_chirde@gmail.com",
                "phone" : "9874563217",
                }
                driver.find_element(
                By.XPATH, '//*[@id="create_user"]/div/div[1]/input[2]'
                ).send_keys(test_input["name"])
                
                driver.find_element(
                By.XPATH, '//*[@id="create_user"]/div/div[2]/input'
                ).send_keys(test_input["phone"])
                
                driver.find_element(
                    By.XPATH, '//*[@id="create_user"]/div/div[3]/input'
                ).send_keys(test_input["email"])
                
                driver.find_element(
                By.XPATH, '//*[@id="create_user"]/div/div[4]/input'
                ).send_keys("123456")
                
                driver.find_element(By.XPATH, '//*[@id="status"]').click()
                
                driver.find_element(By.XPATH, '//*[@id="user_type"]').click()
                sleep(2)
                #Task2: 
                  
    #               def user_flow(self):
    # LOGGER.warning("-------------User Tab Testing Started---------------")
    # driver = self.driver

    # # ... (other code remains unchanged)

    # # create validation started
    # test_input = {
    #     "name": "Sanskruti",
    #     "email": "sanskruti_chirde@gmail.com",
    #     "phone": "9874563217",
    # }
    # # Filling user information...

    # # Clicking the button to create the user
    # driver.find_element(By.XPATH, '//*[@id="create_user_btn"]').click()
    # LOGGER.warning("User Created. Validating if the user is visible in the list.")

    # # Checking if the created user is visible in the list
    # created_user_name = test_input["name"]
    # user_visible = False

    # # Wait for the user list to load (adjust the locator as per your application)
    # user_list = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="all_users_data"]'))
    # )
    
    # # Fetching all the user names in the list and verifying the created user
    # user_names = driver.find_elements(By.XPATH, '//*[@id="all_users_data"]/tbody/tr/td[2]')
    # for user in user_names:
    #     if user.text == created_user_name:
    #         LOGGER.warning(f"User '{created_user_name}' is visible in the list.")
    #         user_visible = True
    #         break

    # # Performing assertions or logging based on user visibility
    # if user_visible:
    #     # Perform further actions or assertions if required
    #     pass
    # else:
    #     LOGGER.warning(f"User '{created_user_name}' is not visible in the list.")
    #     # You may choose to raise an assertion error or log further details here
    #     pass
                
                sleep(5)
                # dropdownbox = driver.find_elements(by=By.TAG_NAME, value="option")
                driver.find_element(By.XPATH, '//*[@id="create_user_btn"]').click()
                LOGGER.warning("------------User Tab  Testing End ------------");
                break
            except:
                sleep(5)
                pass
            
        #     def _testLoginPasswordValidation(self, driver, validation_error):
        # driver.find_element(By.XPATH, '//*[@id="login_btn"]').click()
           
        # getErrorMsg = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
        #                     (By.CSS_SELECTOR, '#toast-container > div > .toast-message'))).text
                
        # if getErrorMsg.strip() == validation_error.strip():
        #     LOGGER.warning("Phone Number and Password Validation Passed")
        # else:
        #     LOGGER.warning("Validation Error")
        #     return
            
            # Test cases
            sleep(2)
            test_name_field_value = driver.find_element(By.XPATH, '//*[@id="all_users_data"]/tbody/tr[1]/td[2]').text
            self.assertEqual("fdksjffklajflas", test_name_field_value, "match name field")

        sleep(2)
        # second task: click edit buton then change name and click on update
        while True:
            try:
                driver.find_element(
                    By.XPATH, '//*[@id="all_users_data"]/tbody/tr/td[7]/a[1]'
                ).click()
                
                driver.find_element(
                    By.XPATH, '//*[@id="create_user"]/div/div[1]/input[2]'
                ).clear()
                
                driver.find_element(
                    By.XPATH, '//*[@id="create_user"]/div/div[1]/input[2]'
                ).send_keys("Sanskruti QA")
                
                driver.find_element(By.XPATH, '//*[@id="create_user_btn"]').click()
                sleep(5)
                
                break
            except:
                sleep(5)
                pass

    def validate_field(self, current_txt, validated_txt, warning_txt):
        if current_txt.strip() == validated_txt.strip():
            LOGGER.warning(warning_txt)
        else:
            LOGGER.warning("Validation Error")
            print("\n\n")
            return

    def goal_flow(self):
        while True:
            try:
                driver = self.driver
                driver.find_element(
                    By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[2]/a'
                ).click()
                
                driver.find_element(
                    By.XPATH, '//*[@id="goal_form"]/div/div[1]/input[2]'
                ).send_keys("demo Testing")
                
                driver.find_element(
                    By.XPATH, '//*[@id="goal_form"]/div/div[2]/input'
                ).send_keys("1")
                select_is_child = Select(
                    driver.find_element(By.XPATH, '//*[@id="is_child"]')
                )
                select_is_child.select_by_index(1)
                driver.find_element(By.XPATH, '//*[@id="goal_btn"]').click()
                sleep(5)
                
                break
            except:
                sleep(5)
                pass
            
    def activity_flow(self):
        while True:
            try:
                driver = self.driver
                driver.find_element(
                    By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[3]/a/span'
                ).click()
                
                driver.find_element(
                    By.XPATH, '//*[@id="activity_form"]/div/div[1]/input[2]'
                ).send_keys("drinking")
                
                driver.find_element(
                    By.XPATH, '//*[@id="activity_form"]/div/div[2]/input'
                ).send_keys("1")
                
                select_is_child = Select(
                    driver.find_element(By.XPATH, '//*[@id="is_child"]')
                )
                select_is_child.select_by_index(1)   
                        
                select_is_adult = Select(
                    driver.find_element(By.XPATH, '//*[@id="is_adult"]')
                )
                select_is_adult.select_by_index(1)
                
                select_is_activity_status = Select(
                    driver.find_element(By.XPATH, '//*[@id="activity_status"]')
                )
                select_is_activity_status.select_by_index(1)
                
                driver.find_element(By.XPATH, '//*[@id="activity_btn"]').click()
                sleep(5)
                
                break
            except:
                sleep(5)
                pass
            
    def symptoms_flow(self):
        while True:
            try:
                driver = self.driver
                driver.find_element(
                    By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[5]/a'
                ).click()
                driver.find_element(
                    By.XPATH, '//*[@id="symptom_form"]/div/div[1]/input[2]'
                ).send_keys("Demo")
                driver.find_element(
                    By.XPATH, '//*[@id="symptom_form"]/div/div[2]/input'
                ).send_keys("1")
                select_is_child = Select(
                    driver.find_element(By.XPATH, '//*[@id="is_child"]')
                )
                select_is_child.select_by_index(1)
                select_is_adult = Select(
                    driver.find_element(By.XPATH, '//*[@id="is_adult"]')
                )
                select_is_adult.select_by_index(1)
                select_symptom_status = Select(
                    driver.find_element(By.XPATH, '//*[@id="symptom_status"]')
                )
                select_symptom_status.select_by_index(1)
                select_zone = Select(
                    driver.find_element(By.XPATH, '//*[@id="zone"]')
                )
                select_zone.select_by_index(1)
                driver.find_element(By.XPATH, '//*[@id="symptom_btn"]').click()
                break
            except:
                sleep(5)
                pass
            
    def symptoms_flow(self):
        while True:
            try:
                driver = self.driver
                driver.find_element(
                    By.XPATH, '//*[@id="main-menu-navigation"]/li[2]/ul/li[5]/a'
                ).click()
                
                driver.find_element(
                    By.XPATH, '//*[@id="symptom_form"]/div/div[1]/input[2]'
                ).send_keys("Demo")
                
                driver.find_element(
                    By.XPATH, '//*[@id="symptom_form"]/div/div[2]/input'
                ).send_keys("1")
                
                break
            except:
                sleep(5)
                pass
                
             
    def tearDown(self):
        self.driver.quit()

if _name_ == '_main_':
    pinktree_test = PinktreeIntegrationTest()
    pinktree_test.setUp()