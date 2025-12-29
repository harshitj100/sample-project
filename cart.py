from data import carts, products


def add_to_cart(username, product_id, quantity):
    if username not in carts:
        carts[username] = {}
    carts[username][product_id] = carts[username].get(product_id, 0) + quantity
    print("Item added to cart")


def view_cart(username):
    if username not in carts or not carts[username]:
        print("Cart is empty")
        return 0

    total = 0
    print("\nYour Cart:")
    for pid, qty in carts[username].items():
        product = products[pid]
        cost = product["price"] * qty
        total += cost
        print(f"{product['name']} x {qty} = ₹{cost}")
    print(f"Total: ₹{total}")
    return total


def clear_cart(username):
    carts[username] = {}
