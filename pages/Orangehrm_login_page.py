from selenium.webdriver.common.by import By


class Login:
    heading_Login_xpath = "//h5[text()='Login']"
    p_username_xpath = "//p[text()='Username : Admin']"
    p_password_xpath = "//p[text()='Password : admin123']"
    label_username_xpath = "//label[text()='Username']"
    label_password_xpath = "//label[text()='Password']"
    txtbx_username_name = "username"
    txtbx_password_name = "password"
    button_login_xpath = "//button[text()=' Login ']"
    p_forgot_password_xpath = "//p[text()='Forgot your password?']"
    link_profilename_classname="oxd-userdropdown-name"
    link_logout_linktext="Logout"
    p_invalid_credentials_xpath="//p[text()='Invalid credentials']"

    def __init__(self, driver):
        self.driver = driver

    def verify_Login_Heading(self):
        actual_text_heading = self.driver.find_element(By.XPATH, self.heading_Login_xpath).text
        return actual_text_heading

    def verify_username_details(self):
        actual_username_text = self.driver.find_element(By.XPATH, self.p_username_xpath).text
        return actual_username_text

    def verify_password_details(self):
        actual_password_text = self.driver.find_element(By.XPATH, self.p_password_xpath).text
        return actual_password_text

    def verify_username_label(self):
        actual_username_text = self.driver.find_element(By.XPATH, self.label_username_xpath).text
        return actual_username_text

    def verify_password_label(self):
        actual_password_text = self.driver.find_element(By.XPATH, self.label_password_xpath).text
        return actual_password_text

    def verify_username_textbox(self, username):
        self.driver.find_element(By.NAME,self.txtbx_username_name).send_keys(username)

    def verify_password_textbox(self,password):
        self.driver.find_element(By.NAME,self.txtbx_password_name).send_keys(password)

    def verify_login_button(self):
        actual_login_btn_text=self.driver.find_element(By.XPATH,self.button_login_xpath).text
        return actual_login_btn_text

    def verify_login_button_click(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def verify_forgot_password(self):
        actual_forgot_password_text=self.driver.find_element(By.XPATH,self.p_forgot_password_xpath).text
        return actual_forgot_password_text

    def verify_forgot_password_click(self):
        self.driver.find_element(By.XPATH, self.p_forgot_password_xpath).click()

    def verify_Logout(self):
        self.driver.find_element(By.CLASS_NAME,self.link_profilename_classname).click()
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

    def verify_Invalid_credentials(self):
        actual_Invalid_credentials=self.driver.find_element(By.XPATH,self.p_invalid_credentials_xpath).text
        return actual_Invalid_credentials