import time
import pytest
from selenium.webdriver.common.by import By
from testdata.exceldata import ExcelData
from pageobject.HomePage import HomePage 
from pageobject.CheckoutPage import CheckOutPage 

from utility.BaseClass import BaseClass
# DO NOT NEED THIS @pytest.mark.usefixtures("setup")
# Because this has been imported from the base class

@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        # Functionally calling each locator
        # self.driver.find_element(By.LINK_TEXT,"Shop").click()

        # Using the page object model to invoke each element from it's specific page
        logging = self.get_logging()
        homepage = HomePage(self.driver)
        check_out_page = CheckOutPage(self.driver)

        homepage.shopItems().click()
        logging.info("Getting all the card titles")
        check_out_page.get_card_title().click()
        logging.info("Checkout the phone")
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
        logging.info("Purchasing the phone")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        self.driver.find_element(By.XPATH, "//input[@id = 'country']").send_keys("Ind")
        self.verify_element_presence("//div[@class = 'suggestions']/ul/li/a")
        logging.info("Selecting the country")
        list_of_country = self.driver.find_elements(By.XPATH,"//div[@class = 'suggestions']/ul/li/a")

        for country in list_of_country:
            if country.text == "India":
                country.click()
                break
        
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH,"//input[@value = 'Purchase']").click()

        # Calling a utility method to invoke explicit wait of selenium
        self.verify_element_presence("//div[@class='alert alert-success alert-dismissible']")
        logging.info(self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text)

@pytest.mark.smoke
@pytest.mark.usefixtures("setup2")
class TestTwo(BaseClass):
    
    # def test_download(self):
    #     logging = self.get_logging()
    #     self.driver.find_element(By.ID,"downloadButton").click()

    def test_upload(self,getFruitPrice):
        getFruit = "Mango"
        ExcelData.update_fruit_price(getFruit,getFruitPrice)
        file_path = "/Users/ajaysingh/Downloads/download.xlsx"
        logging = self.get_logging()
        logging.info("Uploading excel")
        file_input = self.driver.find_element(By.CSS_SELECTOR,"input[type='file']")
        file_input.send_keys(file_path)
        self.verify_element_presence("//div[@role='alert' and @class='Toastify__toast-body']")
        message = "Updated Excel Data Successfully."
        web_text = self.driver.find_element(By.XPATH, "//div[text()='Updated Excel Data Successfully.']").text
        assert message == web_text
        print("Uploaded Successfully")
        price_colum = self.driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
        assert getFruitPrice == self.driver.find_element(By.XPATH,"//div[text()='"+getFruit+"']/parent::div/parent::div/div[@data-column-id='"+price_colum+"']/div").text
        self.driver.refresh()
        time.sleep(4)

    
    @pytest.fixture(params=["250","100"])
    def getFruitPrice(self, request):
        return request.param
