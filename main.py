from auth import login, register
from products import list_products
from cart import add_to_cart, view_cart
from orders import place_order, view_orders


def user_menu(username):
    while True:
        print("""
1. View Products
2. Add to Cart
3. View Cart
4. Place Order
5. View Orders
6. Logout
""")
        choice = input("Choose option: ")

        if choice == "1":
            list_products()

        elif choice == "2":
            pid = int(input("Product ID: "))
            qty = int(input("Quantity: "))
            add_to_cart(username, pid, qty)

        elif choice == "3":
            view_cart(username)

        elif choice == "4":
            place_order(username)

        elif choice == "5":
            view_orders(username)

        elif choice == "6":
            break

        else:
            print("Invalid choice")


def main():
    while True:
        print("""
1. Login
2. Register
3. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            user = login()
            if user:
                user_menu(user)

        elif choice == "2":
            user = register()
            if user:
                user_menu(user)

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
