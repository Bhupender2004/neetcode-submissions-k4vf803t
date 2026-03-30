public class Solution {
    public int buyChoco(int[] prices, int money) {
        Arrays.sort(prices);
        int buy = prices[0] + prices[1];
       if (buy > money) {
             return money;
        } else {
            return money - buy;
        }
    }
}