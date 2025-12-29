from data import products


def list_products():
    print("\nAvailable Products:")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ₹{info['price']}")


def get_product(product_id):
    return products.get(product_id)
