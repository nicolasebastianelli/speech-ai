import os

from .logger import logger


def create_directory_from_path(filepath):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            logger.info("Directory '%s' created.", directory)
        except OSError as error:
            logger.error("An error occurred while creating directory. Error details: %s", error)
