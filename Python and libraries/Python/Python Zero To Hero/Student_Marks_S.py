from functools import reduce

def order_status(func):
    def wrapper(self):
        print("\nProcessing Order")
        result = func(self)
        print('Order Successful!')
        return result
    return wrapper

class Customer:

    def __init__(self, name, customer_id, city):
        self.name = name                        
        self.customer_id = customer_id
        self.city = city

        def show_details(self):
            return {
                "Name": self.name,
                "Customer_id": self.customer_id,
                "City" : self.city
            }

class Product:

    def __init__(self, product_name, price, quantity):
        if price <= 0 or quantity <= 0:
            raise ValueError("Invalid price or quality")
    self.product_name = product_name
    self.price = price
    self.quantity = quantity  

    def show_product(self):
        return f"{self.product_name} - {self.price}"

    def update_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Invalid Quantity")
        
        self.quantity = quantity


class Order:
    

