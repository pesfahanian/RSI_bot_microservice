import logging

from cryptofeed import FeedHandler
from cryptofeed.callback import Callback
from cryptofeed.defines import CANDLES
from cryptofeed.exchanges import BinanceFutures

from schema import FeedConfiguration

logger = logging.getLogger(__name__)


class BinanceUSDMFeed:
    name = r'Binance USDⓈ-M'

    def __init__(self, configuration: FeedConfiguration) -> None:
        logger.info(f'Initializing {self.name} data-feed...')

        self.configuration = configuration

        self.__current_price: float = None
        self.__current_hurst: float = None

        # self.postgres_handler = PostgresHandler()

        self.__setup_handler()
        self.__add_all_feeds()

        logger.info(f'{self.name} data-feed initialized!')

    def run(self) -> None:
        try:
            logger.info('Proceding to run the data-feed...')
            self.handler.run()
            logger.info('Data-feed is running!')
        except Exception as e:
            raise Exception(f'Data-feed failed to run. Reason: {str(e)}.')

    def __setup_handler(self) -> None:
        try:
            logger.info(f'Setting up the {self.name} handler...')
            self.handler = FeedHandler()
            logger.info(f'{self.name} handler is set-up!')

        except Exception as e:
            raise Exception(f'Failure in setting up the {self.name} handler. '
                            f'Reason: {str(e)}.')

    def __add_all_feeds(self) -> None:
        logger.info('Adding all the feeds...')
        for feed in self.__feeds:
            self.__add_feed(feed=feed)
        logger.info('All feeds added!')

    def __add_feed(self, feed: BinanceFutures) -> None:
        try:
            self.handler.add_feed(feed)
        except Exception as e:
            raise Exception(f'Failure to add the feed `{feed}`. '
                            f'Reason: {str(e)}.')

    async def __ohlcv_callback(self, **kwargs) -> None:
        if kwargs['closed']:
            print(kwargs)
            # self.postgres_handler.insert_cndlh(
            #     timestamp=kwargs['timestamp'],
            #     open=float(kwargs['open_price']),
            #     high=float(kwargs['high_price']),
            #     low=float(kwargs['low_price']),
            #     close=float(kwargs['close_price']),
            #     hurst=self.__current_hurst)

    @property
    def __feeds(self) -> list:
        return [self.__ohlcv_feed]

    @property
    def __ohlcv_feed(self) -> BinanceFutures:
        try:
            logger.info('Creating the `OHLCV` feed...')
            feed = BinanceFutures(
                symbols=[self.configuration.symbol],
                channels=[CANDLES],
                callbacks={CANDLES: Callback(self.__ohlcv_callback)})
            logger.info('`OHLCV` feed created!')
            return feed

        except Exception as e:
            raise Exception('Failure in creating the `OHLCV` feed. '
                            f'Reason: {str(e)}.')

    @property
    def current_price(self) -> float:
        return self.__current_price

    @property
    def current_hurst(self) -> float:
        return self.__current_hurst
