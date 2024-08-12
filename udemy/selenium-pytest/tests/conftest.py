import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-dev-shm-usage')

def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='Select the browser'
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser")
    url = "https://rahulshettyacademy.com/angularpractice/"
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(url)
    request.cls.driver = driver
    yield
    print("Closing the browser")
    driver.close()


@pytest.fixture(scope="class")
def setup2(request):
    browser_name = request.config.getoption("browser")
    url = "https://rahulshettyacademy.com/upload-download-test/index.html"
    print("Opening the browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    print("Closing the browser")
    driver.close()