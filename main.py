import log
import sub
from logging import getLogger

dir = './Log/'
logger = getLogger(__name__)
log.set_log_config(logger, dir, 'main.log' )

# subのテストメソッド呼び出し
sub.test_method(dir)

# main内のlogger出力
logger.info('--------------------')
logger.info('Main: 完了')