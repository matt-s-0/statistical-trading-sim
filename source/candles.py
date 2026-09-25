import tkinter as tk
import timestamp

class Candle():
    def __init__(self, OpeningPrice: float, ClosingPrice: float, HighPrice: float, LowPrice: float, TimeStamp: timestamp.SmallTimeStamp | None = None) -> None:
        self.OpeningPrice = OpeningPrice
        self.ClosingPrice = ClosingPrice

        self.HighPrice = HighPrice
        self.LowPrice = LowPrice

        if TimeStamp:
            self.TimeStamp = TimeStamp

def renderCandles(window: tk.Tk, CandleData: list[Candle]) -> None:
    MaxPrice = 0
    MinPrice = 0

    for C in CandleData:
        if type(C) != Candle:
            print(f"Item in candle list is not a candle:\n{C}")
            pass

        MaxPrice = max(MaxPrice, C.HighPrice)
        MinPrice = min(MinPrice, C.LowPrice)