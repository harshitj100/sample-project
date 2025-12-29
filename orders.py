from data import orders
from cart import view_cart, clear_cart


def place_order(username):
    total = view_cart(username)
    if total == 0:
        print("Nothing to order")
        return

    order_id = len(orders) + 1
    orders[order_id] = {
        "user": username,
        "total": total
    }
    clear_cart(username)
    print(f"Order placed successfully. Order ID: {order_id}")


def view_orders(username):
    print("\nYour Orders:")
    found = False
    for oid, info in orders.items():
        if info["user"] == username:
            print(f"Order {oid} - Total ₹{info['total']}")
            found = True
    if not found:
        print("No orders found")
