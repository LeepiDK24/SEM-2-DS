class StockSpanner:

    def __init__(self):
        self.price = []
        self.span = [] 

    def next(self, price: int) -> int:
        span = 1
        while self.price and self.price[-1] <= price:
            self.price.pop()
            span += self.span.pop()
        self.price.append(price)
        self.span.append(span)
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)