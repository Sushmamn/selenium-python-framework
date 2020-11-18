import logging
import inspect


def customLogger(log_level = logging.DEBUG):
    loggerName = inspect.stack()[1][3]      # Gets the filename from which log messages are printed
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)      # By default, log all messages

    filehandler = logging.FileHandler("automation.log", "a")
    filehandler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger
