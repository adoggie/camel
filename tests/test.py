import logging

# create logger
logger_name = "example"
logger = logging.getLogger(logger_name)
# logger.setLevel(logging.DEBUG)

# create file handler
log_path = "./log.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
# formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
# fh.setFormatter(formatter)
logger.addHandler(fh)
sh = logging.StreamHandler()
# logger.addHandler(sh)
# print log info
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message ccc')

