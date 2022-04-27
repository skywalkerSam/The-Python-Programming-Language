"""
Dev: Starboy
Aim: Just testing...
Log: 12022.01.31.04:35
"""

amazon_cart = [
    "A Powerful Laptop",
    "A Mechanical Keyboard",
    "A Fast, Customizable & Comfortable Mouse",
    "A Tough Backpak For My Powerful Laptop",
    "A Multipurpose Toolbox",
    "A Desktop pad, 90*45cm",
    "A Type-C to HDMI connector, G-Sync Compatible"
]
print("\n")
i=1
for item in amazon_cart:
    print(i,"- ", item)
    i += 1


cart_price = amazon_cart.copy()
cart_price[0] = 115000
cart_price[1] = 2500
cart_price[2] = 2100
cart_price[3] = 3000
cart_price[4] = 1000
cart_price[5] = 1000
cart_price[6] = 1200

print("\n")
i=1
for price in cart_price:
    print(i,"- ", price)
    i += 1


print("\nTotal Cart Price: Rs.", sum(cart_price), "/-")

