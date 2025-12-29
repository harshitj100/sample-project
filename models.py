class User:
    def __init__(self, username):
        self.username = username


class CartItem:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity


class Order:
    def __init__(self, order_id, username, items, total):
        self.order_id = order_id
        self.username = username
        self.items = items
        self.total = total
