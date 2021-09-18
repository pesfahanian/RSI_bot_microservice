from dataclasses import dataclass


@dataclass
class FeedConfiguration:
    base: str
    quote: str
    symbol: str = None

    def __post_init__(self) -> None:
        self.symbol = f'{self.base.upper()}-{self.quote.upper()}-PERP'
