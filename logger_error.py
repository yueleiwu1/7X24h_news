


import logging

logger = logging.getLogger('newslog')
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
filehandler = logging.FileHandler('newslog3.txt')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.setLevel(logging.INFO)

def logError(*args):
    logger.error(args)
