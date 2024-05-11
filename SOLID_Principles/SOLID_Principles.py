from abc import ABC, abstractmethod

# SRP: Single Responsibility Principle
class User:
    def __init__(self, name: str):
        self.name = name

# OCP: Open/Closed Principle
class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass

class VIPDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.9

class SuperVIPDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.8

# LSP: Liskov Substitution Principle
def calculate_price(discount: Discount, price: float) -> float:
    return discount.apply(price)

# ISP: Interface Segregation Principle
class Order:
    def __init__(self, user: User, price: float, discount: Discount):
        self.user = user
        self.price = price
        self.discount = discount

    def final_price(self) -> float:
        return calculate_price(self.discount, self.price)

# DIP: Dependency Inversion Principle
class DiscountFactory:
    @staticmethod
    def get_discount(user: User) -> Discount:
        if user.name == 'VIP':
            return VIPDiscount()
        elif user.name == 'SuperVIP':
            return SuperVIPDiscount()
        else:
            raise ValueError('Unsupported user type')

# Usage
user = User('SuperVIP')
order = Order(user, 100.0, DiscountFactory.get_discount(user))
print(f"The final price is: {order.final_price()}")