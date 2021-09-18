import logging

import json

from schema import FeedConfiguration

import settings  # noqa

logger = logging.getLogger(__name__)


def read_configuration() -> FeedConfiguration:
    try:
        logger.info('Reading the configuration file...')
        with open(settings.CONFIGURATION_PATH, 'r+') as f:
            configuration = json.load(f)
        logger.info('Configuration file read!')
        return FeedConfiguration(base=configuration['base'],
                                 quote=configuration['quote'])
    except Exception as e:
        raise Exception('Failure in reading the configuration '
                        f'file. Reason: {str(e)}.')
