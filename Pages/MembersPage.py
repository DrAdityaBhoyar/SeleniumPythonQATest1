from selenium.webdriver.common.by import By


class MembersPage:
    def __init__( self, driver):
        self.driver = driver

    # Locators
    _membersTab_ = (By.XPATH, "//a[text()='MEMBERS']")
    _addMemberButton_ = (By.ID, "add_new_member")
    _memberEmail_ = (By.ID, "user_email")
    _memberFirstName_ = (By.ID, "first_name")
    _memberLastName_ = (By.ID, "last_name")
    _createMemberButton_ = (By.XPATH, "//a[text()='ADD']")
    _newUserSuccessMessage_ = (By.ID, "enroll_user_success")
    _searchBox_ = (By.XPATH, "//input[@type='text'][@placeholder='Search by name, email, phone number, member id']")
    _searchBoxButton_ = (By.XPATH, "//*[@class='sprite search']")
    _selectAllCheckboxes_ = (By.XPATH, "//input[@type='checkbox'][@id='all_users']")
    _actionsTab_ = (By.CSS_SELECTOR, "div[id='user_management_actions']")
    _deleteButton_ = (By.XPATH, "//li[text()='Delete']")
    _alertConfirmButton_ = (By.XPATH, "//button[text()='Confirm']")

    def test_navigateMembersTab( self ):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._membersTab_).click()

    def test_clickAddMemberButton(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._addMemberButton_).click()

    def test_addNewMember(self, memberEmail, memberFirstName, memberLastName):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._memberEmail_).send_keys(memberEmail)
        self.driver.find_element(*MembersPage._memberFirstName_).send_keys(memberFirstName)
        self.driver.find_element(*MembersPage._memberLastName_).send_keys(memberLastName)
        self.driver.find_element(*MembersPage._createMemberButton_).click()
        self.driver.find_element(*MembersPage._newUserSuccessMessage_).click()

    def test_addValidMember(self, memberEmail, memberFirstName, memberLastName):
        addMember = MembersPage(self.driver)
        addMember.test_navigateMembersTab()
        addMember.test_clickAddMemberButton()
        addMember.test_addNewMember(memberEmail, memberFirstName, memberLastName)

    def test_searchMember(self, memberEmail):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._searchBox_).click()
        self.driver.find_element(*MembersPage._searchBox_).send_keys(memberEmail)
        self.driver.find_element(*MembersPage._searchBoxButton_).click()

    def test_selectCheckBoxMember(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._selectAllCheckboxes_).click()

    def test_searchAndSelectMember(self, memberEmail):
        ss = MembersPage(self.driver)
        ss.test_searchMember(memberEmail)
        ss.test_selectCheckBoxMember()

    def test_navigateActionsTab(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._actionsTab_).click()

    def test_deleteButton(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._deleteButton_).click()

    def test_confirmButton(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*MembersPage._alertConfirmButton_).click()

    def test_deleteMember(self):
        dm = MembersPage(self.driver)
        dm.test_navigateActionsTab()
        dm.test_deleteButton()
        dm.test_confirmButton()






















