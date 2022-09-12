from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.Orangehrm_login_page import Login
from utility.ReadConfig import ReadConfig


class Test_Login_TC_001:
    base_url = ReadConfig.getApp()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_verifyTitle(self,setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_title = self.driver.title
        if actual_title == "OrangeHRM":
            assert True
            print("Test pass")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_verifyTitle_TC_001.png")
            print("Test fail")
            self.driver.close()
            assert False

    def test_verifyCurrent_url(self,setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        actual_url = self.driver.current_url
        if actual_url == self.base_url:
            assert True
            print("Test pass")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_verifyCurrent_Url_TC_002.png")
            print("Test fail")
            self.driver.close()
            assert False

    def test_verify_Login_heading(self,setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        lp = Login(self.driver)
        actual_heading = lp.verify_Login_Heading()
        if actual_heading == "Login":
            assert True
            print("Test pass")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_verify_login_heading_TC_003.png")
            print("Test fail")
            self.driver.close()
            assert False

    def test_verify_username_notes(self,setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        lp = Login(self.driver)
        actual_username_details = lp.verify_username_details()
        if actual_username_details == "Username : Admin":
            assert True
            print("Test pass")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_verify_username_notes_TC_004.png")
            print("Test fail")
            self.driver.close()
            assert False
