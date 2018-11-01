# -*- coding: utf-8 -*-

# logging
import logging

logging.basicConfig(filename='logger01.log')
logger1=logging.getLogger()
logger1.info('what')  # nothing in log file

print(logger1.level)

# levels : debug, Info, warning, error, critical
logging.basicConfig(filename='logger01.log', level = logging.DEBUG)
logger1=logging.getLogger()
logger1.info('what')

# where to find log_formats: ...
log_format = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='logger01.log',  file_mode = 'a', level = logging.DEBUG, format = log_format)
logger1=logging.getLogger()
logger1.info('what')