from typing import List

def maxProfit(self, prices: List[int]) -> int:
    min = prices[0]
    max = 0
    for number in prices:
        if number < min:
            min = number
        if number - min > max:
            max = number - min
    return max
