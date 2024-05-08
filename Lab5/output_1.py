class ProductSearchStrategy:
    @staticmethod
    def search_product(products, query):
        pass

class SearchByNameStrategy(ProductSearchStrategy):
    @staticmethod
    def search_product(products, query):
        result = []
        for product in products:
            if query.lower() in product.name.lower():
                result.append(product)
        return result

class SearchByTypeStrategy(ProductSearchStrategy):
    @staticmethod
    def search_product(products, query):
        result = []
        for product in products:
            if query.lower() == product.type.lower():
                result.append(product)
        return result

class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def display_product(self):
        print(f"Name: {self.name}, Price: {self.price}, Type: {self.type}")

class ProductManager:
    def __init__(self, products):
        self.products = products

    @staticmethod
    def search_product(products, query, search_strategy):
        return search_strategy.search_product(products, query)

    @staticmethod
    def display_products(products):
        for product in products:
            product.display_product()

# Приклад використання:
products = [
    Product("Phone", 500, "Electronics"),
    Product("Laptop", 1000, "Electronics"),
    Product("Shirt", 20, "Clothing"),
    Product("Pants", 30, "Clothing")
]

result = ProductManager.search_product(products, "shirt", SearchByNameStrategy())
ProductManager.display_products(result)

result = ProductManager.search_product(products, "Electronics", SearchByTypeStrategy())
ProductManager.display_products(result)
