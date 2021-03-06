from logging import StreamHandler, DEBUG, INFO, Formatter, getLogger
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import os

def set_log_config(logger, dir, filename):

    # ---- Prepare log folder ----
    os.makedirs(dir, exist_ok=True) 
    filepath = dir + filename

    # ---- handler1: For terminal ----
    handler1 = StreamHandler()
    handler1.setLevel(DEBUG)
    handler1.setFormatter(Formatter("[%(asctime)s][%(levelname)8s][%(name)s][%(funcName)s] %(message)s"))

    # ---- handler2: For log file ----
    #handler2 = TimedRotatingFileHandler(filename = filepath, when='midnight', backupCount=30, encoding='utf-8') # If you want to rotate file by time, use this
    handler2 = RotatingFileHandler(filename = filepath, maxBytes = 1048576, backupCount = 10, encoding='utf-8', ) # 1MB, keep 10 files
    handler2.setLevel(INFO)
    handler2.setFormatter(Formatter("[%(asctime)s][%(levelname)8s][%(name)s][%(funcName)s] %(message)s"))

    # ---- Set log config ----
    logger.setLevel(DEBUG)
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    logger.propagate = False

# To check module operation
if __name__ == '__main__':
    
    dir = './Log/'
    logger = getLogger(__name__)
    set_log_config(logger, dir, 'log_filename.log' )

    try:
        logger.debug('Test: debug')
        logger.info('Test: info')
        logger.warn('Test: warn')
        logger.error('Test: error')
        logger.critical('Test: critical')
        
        # NameError: name 'b' is not defined
        a = b

    except Exception as e:
        logger.exception('Test: exception')
