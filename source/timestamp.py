class SmallTimeStamp:
    def __init__(self, Seconds: int, Minutes: int, Hours: int) -> None:
        TotalSeconds = Seconds + Minutes * 60 + Hours * 3600

        self.Hours = TotalSeconds // 3600
        TotalSeconds %= 3600

        self.Minutes = TotalSeconds // 60
        self.Seconds = TotalSeconds % 60

        self.TotalSeconds = TotalSeconds