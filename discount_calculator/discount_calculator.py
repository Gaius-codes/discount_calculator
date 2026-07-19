from abc import ABC, abstractmethod

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product) -> bool:
        return product.price <= 70
    
    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

product = Product("Laptop", 1000)

discount = PercentageDiscount(25)
print(discount.apply_discount(product))
