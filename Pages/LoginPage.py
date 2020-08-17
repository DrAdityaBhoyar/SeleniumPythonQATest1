from selenium.webdriver.common.by import By


class LoginPage:
    def __init__( self, driver):
        self.driver = driver

    # Locators
    _emailId_ = (By.ID, "id_email")
    _password_ = (By.ID, "id_password")
    _loginButton_ = (By.ID, "id_login_button")

    def test_emailId(self, emailId):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*LoginPage._emailId_).send_keys(emailId)

    def test_password(self, password):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*LoginPage._password_).send_keys(password)

    def test_loginButton(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*LoginPage._loginButton_).click()

    def test_validLogin(self, email, password):
        lp = LoginPage(self.driver)
        lp.test_emailId(email)
        lp.test_password(password)
        lp.test_loginButton()


