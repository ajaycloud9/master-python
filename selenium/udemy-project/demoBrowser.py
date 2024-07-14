import time
import warnings
from urllib3.exceptions import NotOpenSSLWarning
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Suppress the specific NotOpenSSLWarning
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL 1.1.1+.*")
# driver = webdriver.Chrome()

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

def execise_0():
    # Excercise - 0 (Find eleement from static dropdown)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element_by_xpath("//input [@name='name' and @required]").send_keys("Ajay Singh")
    driver.find_element(By.XPATH,"(//input [@name='name'])[1]").send_keys("Ajay Singh")

    #Select static dropdown
    dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
    dropdown.select_by_visible_text("Female")
    dropdown.select_by_index(0)

def excercise_1():
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element(By.ID, "autosuggest").send_keys("ind")
    time.sleep(2)
    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

    for country in countries:
        print(country.text)
        if country.text == "India":
            country.click()
            break
    # Important thing to note here that inorder to get what we typed 
    # We need to make sure that we need to get that value using get_attribute
    # Since the text is not comes by default with the element we need to
    # The text which we entered using the script. Hence, to dynamically written
    # Code we need to make sure, we have enough 
    assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

    # print(driver.title)
    # print(driver.current_url)

# ===========================================================================
# Excercise - 2 Radio Buttons
class AutomationPratice():
    '''
    Pratice excerise 2 and excercise 3
    '''
    my_event = "Global event"
    def __init__(self):
        url = "https://rahulshettyacademy.com/AutomationPractice/"
        driver.get(url)

    def execise_2(self):
        '''
        Radio and checkbox
        '''
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for item in checkboxes:
            print(item.get_attribute("value"))
            print(item.get_attribute("name"))
            if item.get_attribute("value") == "option2":
                item.click()
                assert item.is_selected()
        
        radios = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
        for radio in radios:
            print(radio.get_attribute("value"),"radio")
            if radio.get_attribute("value") == "radio2":
                radio.click()
                assert radio.is_selected()
            print(radio.get_attribute("name"))
        
        assert driver.find_element(By.ID, "displayed-text").is_displayed()
        driver.find_element(By.ID, "hide-textbox").click()
        # We hided the displayed element
        # Checking with negate condition
        assert not driver.find_element(By.ID, "displayed-text").is_displayed()
    
    def execise_3(self):
        '''
        Create a Pop up and,
        assert whether the name in the pop is same or not
        '''
        name = "Ajay"
        driver.find_element(By.XPATH, "//input[@name='enter-name']").send_keys(name)
        driver.find_element(By.XPATH, "//input[@value='Alert']").click()
        alert = driver.switch_to.alert
        alertText = alert.text
        print(alertText)
        assert name in alertText
        alert.accept()

class ShoppingCart():
    def __init__(self):
        url = "https://rahulshettyacademy.com/seleniumPractise/#/"
        driver.get(url)
    
    def exercise_4(self):
        driver.implicitly_wait(2)
        driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
        time.sleep(2)
        results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
        print(len(results))
        for result in results:
            result.find_element(By.XPATH,"div/button").click()
        driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
        driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        cart_items = driver.find_elements(By.XPATH,"//tbody/tr/td/p[@class = 'amount']")
        total_sum = 0
        for index in range(0,len(cart_items),2):
            price = int(cart_items[index].text)
            total_sum += price
        print(total_sum)
        driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
        driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        wait = WebDriverWait(driver,10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".promoInfo")))
        print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

class MouseHover():
    '''
    Pratice excerise 4 and excercise 5
    '''
    def __init__(self) -> None:
        url = "https://rahulshettyacademy.com/AutomationPractice/"
        driver.get(url)

    def excercise5(self):
        '''
        Action hoever and right click
        '''
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
        # action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
        action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

class ChildWindow():
    '''
    Pratice excerise 6
    '''
    
    def execise_6(self):
        url = "https://the-internet.herokuapp.com/windows"
        driver.get(url)
        driver.find_element(By.LINK_TEXT,"Click Here").click()
        windowsOpened = driver.window_handles

        driver.switch_to.window(windowsOpened[1])
        print(driver.find_element(By.TAG_NAME, "h3").text)
        time.sleep(5)
    
    def assignment_1(self):
        url = "https://rahulshettyacademy.com/loginpagePractise/"
        driver.get(url)
        driver.find_element(By.XPATH, "//a[@href='https://rahulshettyacademy.com/documents-request']").click()
        
        windowsOpened = driver.window_handles
        driver.switch_to.window(windowsOpened[1])

        email = driver.find_element(By.XPATH,"//a[@href = 'mailto:mentor@rahulshettyacademy.com']").text
        print(email)
        driver.close()
        driver.switch_to.window(windowsOpened[0])
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(email)
        driver.find_element(By.ID, "password").send_keys("monkey")
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        driver.find_element(By.XPATH, "//input[@name='signin']").click()

        #Select static dropdown
        dropdown = Select(driver.find_element(By.XPATH, "//select"))
        dropdown.select_by_visible_text("Consultant")

        # Explicit wait since we wanted the alert danger element to show up
        wait = WebDriverWait(driver,10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
        print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
        time.sleep(5)
    
    def excercise_7_iFrame(self):
        url = "https://the-internet.herokuapp.com/iframe"
        driver.get(url)
        driver.switch_to.frame("mce_0_ifr")
        body_element = driver.find_element(By.ID, "tinymce")
        driver.execute_script("arguments[0].setAttribute('contenteditable', 'true')", body_element)
        time.sleep(5)
        driver.find_element(By.ID, "tinymce").clear()
        driver.find_element(By.ID, "tinymce").send_keys("Wooho")
        driver.switch_to.default_content()
        time.sleep(5)

class WebTables():

    def sortTables(self):
        url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
        driver.get(url)
        items = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
        my_items = []
        for item in items:
            my_items.append(item.text)
            print(item.text)
        my_items.sort()
        print(my_items)

class End2EndSeleniumAutomation():
    def __init__(self) -> None:
        url = "https://rahulshettyacademy.com/angularpractice/"
        driver.get(url)
        driver.find_element(By.LINK_TEXT,"Shop").click()
        driver.find_element(By.XPATH,"//a[text() = 'Blackberry']/following::button[1]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        driver.find_element(By.XPATH, "//input[@id = 'country']").send_keys("Ind")
        wait = WebDriverWait(driver,10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class = 'suggestions']")))
        list_of_country = driver.find_elements(By.XPATH,"//div[@class = 'suggestions']/ul/li/a")

        for country in list_of_country:
            if country.text == "India":
                country.click()
                break
        
        driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        driver.find_element(By.XPATH,"//input[@value = 'Purchase']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
        print(driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text)






        


# automation_obj = AutomationPratice()
# automation_obj.execise_2()
# automation_obj.execise_3()

# shopping_obj = ShoppingCart()
# shopping_obj.exercise_4()

# mouse_obj = MouseHover()
# mouse_obj.excercise5()

# child_obj = ChildWindow()
# child_obj.excercise_7_iFrame()

# table_obj = WebTables()
# table_obj.sortTables()

End2EndSeleniumAutomation()

driver.quit()
