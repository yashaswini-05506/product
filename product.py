def product_details(name, id, quantity, price):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {id}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result

if __name__ == "__main__":
    # Sample Output
    name = "Lenovo Laptop"
    id = "P1001"
    quantity = 10
    price = 48000
    print(product_details(name, id, quantity, price))