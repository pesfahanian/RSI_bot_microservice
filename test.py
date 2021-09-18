from cryptofeed import FeedHandler
from cryptofeed.callback import Callback
from cryptofeed.defines import CANDLES
from cryptofeed.exchanges import BinanceFutures


async def ohlcv(data):
    print(data)


def main():
    f = FeedHandler()
    f.add_feed(
        BinanceFutures(symbols=['SOL-USDT-PERP'],
                       channels=[CANDLES],
                       callbacks={CANDLES: Callback(ohlcv)}))

    f.run()


if __name__ == '__main__':
    main()
