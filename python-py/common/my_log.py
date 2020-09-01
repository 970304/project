import logging
from common import dir_location


class MyLog:

    def my_log(self, msg, level):

        logger = logging.getLogger("LOG")
        logger.setLevel('DEBUG')

        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")

        fh = logging.FileHandler(dir_location.log_dir+'/py.txt', encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        if level == 'DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)

        logger.removeHandler(fh)
        logger.removeHandler(ch)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


# if __name__ == '__main__':
#     a = MyLog()
#     a.critical('www')
#     a.error('ffff')
#     a.info('rrrr')
#     a.warning('mmmm')





