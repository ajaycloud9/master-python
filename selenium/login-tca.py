from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time 

TCA_USERNAME="username"
TCA_PASSWORD="password"
APP_NAME="es-rapp"
NAMESPACE="default"
HARBOR_REGISTRY_URL="url"
HARBOR_USERNAME="username"
HARBOR_PASSWORD="password"
IMAGE_REF=""

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://10.202.116.238/")
driver.maximize_window( )

def debug_using_page_source():
    #print(network_func_button.get_attribute("outerHTML"))
    time.sleep(5)
    page_source = driver.page_source
    fileToWrite = open("page_source.html", "w")
    fileToWrite.write(page_source)
    fileToWrite.close()

def get_all_button(): 
    buttons = driver.find_elements(By.XPATH, "//button")
    print ("All buttons",len(buttons))
    for button in buttons:
        print(button.text)

driver.implicitly_wait(10)

def login_to_tca ():
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(TCA_USERNAME)
    password_input.send_keys(TCA_PASSWORD)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    
def instantiate_network_function():
    network_func_button = driver.find_element(By.XPATH,"//span[@class='nav-text'][normalize-space()='Network Function']")
    network_func_button.click()
    driver.switch_to.frame("overlay-vnf-catalog")
    driver.find_element(By.XPATH,"//button[@aria-label='Available actions for vmware-energy-saving-2.0.4']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Instantiate']").click()
    driver.switch_to.default_content()
    driver.switch_to.frame("overlay-vnf-inventory")
    name = driver.find_element(By.XPATH, "//input[@id='clr-form-control-1' and @formcontrolname='name']")
    name.send_keys(APP_NAME)
    driver.find_element(By.XPATH,"//button[@aria-label='Select Cloud']").click()
    driver.switch_to.default_content()
    time.sleep(2)
    
    element = driver.find_element(By.XPATH, "//input[@aria-label='Select tcp-cric-dev-rahul']")
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    
    element = driver.find_element(By.XPATH,"//button[normalize-space()='Ok']")
    actions.move_to_element(element).click().perform()
    
    driver.switch_to.frame("overlay-vnf-inventory")
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@aria-label='energy-saving details']").click()
    driver.find_element(By.XPATH, "//input[@formcontrolname='namespace']" ).send_keys(NAMESPACE)
    element = driver.find_element(By.XPATH, "//input[@formcontrolname='useRepoSource' and @value='false' ]")
    actions.move_to_element(element).click().perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@formcontrolname='repoUrl' ]").send_keys(HARBOR_REGISTRY_URL)
    driver.find_element(By.XPATH, "//input[@formcontrolname='username']").send_keys(HARBOR_USERNAME)
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys(HARBOR_PASSWORD)
    driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
    time.sleep(2)
    web_element = driver.find_element(By.XPATH, "//clr-control-helper[contains(text(), 'Energy-saving')]/preceding-sibling::*/input")
    web_element.clear()
    web_element.send_keys(IMAGE_REF)
    time.sleep(5)
    driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
    time.sleep(2)

def review_input():
    len_of_table = driver.find_elements(By.XPATH, "//table[@aria-label='Review - Instance Details']/tbody/tr")
    for i in range(1,len(len_of_table)+1):
        data_1 = driver.find_element(By.XPATH, "//table[@aria-label='Review - Instance Details']/tbody/tr[" + str(i) + "]/th").text
        data_2 = driver.find_element(By.XPATH, "//table[@aria-label='Review - Instance Details']/tbody/tr[" + str(i) + "]/td").text
        print(data_1, data_2)
    len_of_table = driver.find_elements(By.XPATH, "//table[@aria-label='energy-saving Repository']/tbody/tr")
    for i in range(1,len(len_of_table)+1):
        data_1 = driver.find_element(By.XPATH, "//table[@aria-label='energy-saving Repository']/tbody/tr[" + str(i) + "]/th").text
        data_2 = driver.find_element(By.XPATH, "//table[@aria-label='energy-saving Repository']/tbody/tr[" + str(i) + "]/td").text
        print(data_1, data_2)

    image_details = driver.find_elements(By.XPATH, "//table[@aria-label='energy-saving Instantiation Properties']/tbody/tr/td")
    print (image_details[0].text,image_details[1].text)


def invoke_network_function():
    debug_using_page_source()
    webelement = driver.find_element(By.XPATH, "//span[contains(text(), 'Instantiate')]")
    webelement.click()
    time.sleep(40)

def upload_files():
    #//td[normalize-space() ='deployment_profile']/following::button[normalize-space() ='Browse'][1]
    #//input[@aria-label='deployment_profile']
    #//input[@aria-label='runtime_overrides']
    #//td[normalize-space() ='runtime_overrides']/following::button[normalize-space() ='Browse'][1]
    pass


#Main Function
login_to_tca()
instantiate_network_function()
review_input()
invoke_network_function()
driver.quit()



# Explicit wait time
# mywait=WebDriverWait(driver, 100)
# mywait.until(EC.presence_of_all_elements_located((By.XPATH,"//text()='Selenium'")))
