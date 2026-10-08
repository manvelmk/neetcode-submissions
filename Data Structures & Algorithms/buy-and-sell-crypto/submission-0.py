class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_potential = profit = 0
        cheapest = float("inf")
        
        for stock in prices:
            if stock < cheapest:
                cheapest = stock
            else:
                potential = stock - cheapest
                if potential > profit:
                    highest_potential = profit = potential
        
        print(f"Buying at {cheapest} selling at {highest_potential}")
        
        return profit