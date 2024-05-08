class DataAnalyzerBase:
    def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None

class DataAnalyzer(DataAnalyzerBase):
    def calculate_total(self, discount=False, tax_rate=0):
        total = super().calculate_total()
        if discount:
            total *= 0.9  # 10% discount
        total *= (1 + tax_rate)
        return total