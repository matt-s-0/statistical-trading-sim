import tkinter as tk
from source import timestamp
from operator import attrgetter

# Class for storing the data for a single candle.
class candle():
    def __init__(self, OpeningPrice: float, ClosingPrice: float, HighPrice: float, LowPrice: float, TimeStamp: timestamp.smallTimeStamp) -> None:
        # https://www.investopedia.com/trading/candlestick-charting-what-is-it/

        self.OpeningPrice = OpeningPrice
        self.ClosingPrice = ClosingPrice

        self.HighPrice = HighPrice
        self.LowPrice = LowPrice

        self.TimeStamp = TimeStamp

def sortCandlesByTimestamp(CandleData: list[candle]) -> list[candle]:
    # Sorts candle data by the timestamp's total seconds in ascending order
    CandleData = sorted(CandleData, key=attrgetter('TimeStamp.TotalSeconds'))

    return CandleData

# Method to render candles based on current time stamp.
def renderCandles(Canvas: tk.Canvas, CandleData: list[candle], CurrentTime: timestamp.smallTimeStamp) -> None:
    # Gets canvas width & height
    CanvasWidth = Canvas.winfo_width()
    CanvasHeight = Canvas.winfo_height()

     # I need to find the max price of all the candles and the min price of all candles
    # so I can make the chart look better
    MaxPrice = max(CandleData, key=attrgetter('HighPrice')).HighPrice
    MinPrice = min(CandleData, key=attrgetter('LowPrice')).LowPrice

    # temporary??
    ColumnWidth = 30
    CanvasColumnSpacing = 20

    # Gets range of candle prices so I can clamp the Y values of the candles so it doesn't look really weird
    PriceRange = MaxPrice - MinPrice
    YScale = CanvasHeight / PriceRange

    # Iterate through candle data
    for i in range(len(CandleData)):
        C = CandleData[i]

        # If a obj in the list isn't a candle then skip it
        if type(C) != candle and i != 0:
            print(f"Item in candle list is not a candle:\n{C}")
            pass

        if C.OpeningPrice < C.ClosingPrice:
            FillColor = "green"
        else:
            FillColor = "red"

        # x1 = left side x coord
        # y1 = bottom y coord
        # x2 = right side x coord
        # y2 = top y coord

        # Candle body
        x1 = (i* (ColumnWidth + CanvasColumnSpacing)) + 5
        x2 = x1 + ColumnWidth

        y1 = ()
        y2 = ()