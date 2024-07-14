import logging
import inspect

class BaseLogger():

    def test_logging(self):
        loggerName = str(inspect.stack()[1][1])
        # print(loggerName[1])
        # print(loggerName[1][1])
        # print(loggerName[1][2])
        # print(loggerName[1][3])
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