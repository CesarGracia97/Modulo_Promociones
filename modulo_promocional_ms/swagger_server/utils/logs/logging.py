import glob
import logging
from logging.handlers import RotatingFileHandler
import datetime


class Log:

    @staticmethod
    def generate_log():
        """Generador de logs para el microservicio

        Returns:
            function: logging
        """

        now = datetime.datetime.now()
        format_logger = now.strftime('%Y-%m-%d')
        logger = logging.getLogger('')
        logger.setLevel(logging.NOTSET)
        rthandler = RotatingFileHandler(f'''logs/modulo-promocional-api-{format_logger}.log''',
                                        maxBytes=2 * 1024 * 1024, backupCount=5)

        formatter = logging.Formatter('%(asctime)s %(levelname)s | %(message)s')
        rthandler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(rthandler)

        logging.getLogger('apscheduler').setLevel(logging.CRITICAL)

        return logger
