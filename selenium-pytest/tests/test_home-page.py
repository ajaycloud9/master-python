import time
import pytest
from selenium.webdriver.common.by import By
from testdata.homepagedata import HomePageData
from selenium.webdriver.support.select import Select

from utility.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_home_page(self,getdata):
        self.driver.find_element(By.XPATH,"//input [@name='name' and @required]").send_keys(getdata["Firstname"])
        self.driver.find_element(By.XPATH,"(//input [@name='name'])[1]").send_keys(getdata["Lastname"])
        time.sleep(8)
        #Select static dropdown
        dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(0)
        self.driver.refresh()
    
    @pytest.fixture(params=HomePageData.exceltodict("Testcase 2"))
    def getdata(self, request):
        return request.param