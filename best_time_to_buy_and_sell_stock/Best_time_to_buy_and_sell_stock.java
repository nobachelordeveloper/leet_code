package best_time_to_buy_and_sell_stock;

public class Best_time_to_buy_and_sell_stock {
    public int maxProfit(int[] prices) {
        var min = prices[0];
        var max = 0;
        for(int i = 0; i < prices.length; i++) {
            if(prices[i] < min) {
                min = prices[i];
            }
            if(prices[i] - min > max) {
                max = prices[i] - min;
            }
        }
        return max;
    }
}
