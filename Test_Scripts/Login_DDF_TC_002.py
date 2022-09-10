from pages.Orangehrm_login_page import Login
from utility import XLUtils
from utility.ReadConfig import ReadConfig


class Test_Login_DDF_TC_002:
    base_url = ReadConfig.getApp()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".\\Excel_data\\2052022.xlsx"

    def test_verifyLogin(self, setup):

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        lp = Login(self.driver)
        lp.verify_username_textbox(self.username)
        lp.verify_password_textbox(self.password)
        lp.verify_login_button_click()
        lp.verify_Logout()
        self.driver.close()

    def test_verifyLogin_DDF(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        lp = Login(self.driver)
        rows = XLUtils.getRowCount(self.path, "Sheet2")
        for r in range(2, rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet2", r, 1)
            self.pwd = XLUtils.readData(self.path, "Sheet2", r, 2)
            lp.verify_username_textbox(self.user)
            lp.verify_password_textbox(self.pwd)
            lp.verify_login_button_click()
            if self.driver.title == "OrangeHRM":
                XLUtils.writedata(self.path, "Sheet2", r, 3, "Pass")
                assert True
                lp.verify_Logout()
            else:
                print("test failed")
                XLUtils.writedata(self.path, "Sheet2", r, 3, "Fail")
                # actual_Invalid = lp.verify_Invalid_credentials()
               # if actual_Invalid == "Invalid credentials":
                self.driver.save_screenshot(".\\Screenshot\\test_verify_login_heading_TC_003.png")
                self.driver.find_element_by_xpath("/html/head/title").click()
            self.driver.refresh()
