class ProductCalculator:
    def __init__(self, product_prices):
        self.product_prices = product_prices

    def calculate_total_price(self, discount=False, tax_rate=0):
        total_price = 0
        for price in self.product_prices:
            if discount:
                price *= 0.9  # 10% discount
            total_price += price
        total_price *= (1 + tax_rate)
        return total_price

class DiscountedProductCalculator(ProductCalculator):
    def calculate_total_price(self, tax_rate=0):
        return super().calculate_total_price(discount=True, tax_rate=tax_rate)

class TaxIncludedProductCalculator(ProductCalculator):
    def calculate_total_price(self, discount=False):
        return super().calculate_total_price(discount=discount, tax_rate=0.1)