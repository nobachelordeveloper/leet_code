function maxProfit(prices: number[]): number {
  let min = prices[0]
  let max = 0
  prices.forEach((num => {
    if(num < min) {
      min = num;
    }
    if(num - min > max) {
      max = num - min;
    }
  }))
  return max;
}