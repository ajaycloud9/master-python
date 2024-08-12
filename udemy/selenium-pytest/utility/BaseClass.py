import logging
import inspect
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    
    def verify_element_presence(self, text):
        wait = WebDriverWait(self.driver,30)
        wait.until(EC.visibility_of_element_located((By.XPATH,text)))


    def get_logging(self):
        loggerName = str(inspect.stack()[1][1])
        logger = logging.getLogger(loggerName)

        # Giving the location on where to log
        fileHandler = logging.FileHandler('pytest.log')

        # Giving information on what format to log
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        #Now passing the formatter object to the filehandler
        fileHandler.setFormatter(formatter)

        # At this point the fileHandler has both information 
        # Connect the logger object with filehandler
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger