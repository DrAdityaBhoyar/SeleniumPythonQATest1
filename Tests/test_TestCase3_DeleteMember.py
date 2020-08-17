from Driver.BaseClass import BaseClass
from Pages.LoginPage import LoginPage
from Pages.MembersPage import MembersPage


class TestDeleteNewMember(BaseClass):

    def test_validLogin(self):
        lp = LoginPage(self.driver)
        lp.test_validLogin("zinrelo+qa1@gmail.com", "Zinrelo@1")

    def test_searchMember(self):
        ng = MembersPage(self.driver)
        ng.test_navigateMembersTab()
        ng.test_searchAndSelectMember("adi12.bhoyar@gmail.com")

    def test_deleteSearchMember(self):
        ss = MembersPage(self.driver)
        ss.test_deleteMember()




