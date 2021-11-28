import logging


class Logger:

    @staticmethod
    def generate_log():
        logger = logging.getLogger()
        fHandler = logging.FileHandler(
            filename='.//Logs//testcases.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fHandler.setFormatter(formatter)
        logger.addHandler(fHandler)
        logger.setLevel(logging.INFO)
        return logger


