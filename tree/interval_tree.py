from typing import Optional, List, Tuple

class Interval:
    def __init__(self, low: int, high: int, data: any = None):
        self.low = low
        self.high = high
        self.data = data
        self.max = high