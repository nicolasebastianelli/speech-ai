import logging


class Logger:
    def __init__(self, logger_name="speech-ai", level=logging.INFO):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)

        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] (%(name)s) - %(message)s")
        handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger


logger = Logger().get_logger()
