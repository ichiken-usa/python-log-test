import log
from logging import getLogger

def test_method(dir):

    logger = getLogger(__name__)
    log.set_log_config(logger, dir, 'sub.log' )

    for i in range (5):
        logger.info(f'Sub: ループ i={i}')