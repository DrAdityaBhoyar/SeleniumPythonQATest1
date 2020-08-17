from Pages.LoginPage import LoginPage
from Pages.MembersPage import MembersPage
from Driver.BaseClass import BaseClass


class TestSearchNewMember(BaseClass):

    def test_validLogin(self):
        lp = LoginPage(self.driver)
        lp.test_validLogin("zinrelo+qa1@gmail.com", "Zinrelo@1")

    def test_searchMember(self):
        ng = MembersPage(self.driver)
        ng.test_navigateMembersTab()
        ng.test_searchMember("Aditya Bhoyar")




