import logging

def test_logging():
    logger = logging.getLogger(__name__)

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

    logger.debug("A debug")
    logger.info("An info")
    logger.warning("A warning")
    logger.error("An error")
    logger.critical("Critical issues")
