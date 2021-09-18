import logging

from binanceusdm import BinanceUSDMFeed

from settings.logger import setup_logging

from utils import read_configuration

logger = logging.getLogger(__name__)
setup_logging()


def main() -> None:
    configuration = read_configuration()
    feed = BinanceUSDMFeed(configuration=configuration)
    feed.run()


if __name__ == '__main__':
    main()
