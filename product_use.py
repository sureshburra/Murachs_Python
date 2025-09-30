from objects import Product

product1 = Product("Stanley Hammer", 12.99, 62)
product2 = Product("National Hardware", 5.06, 0)

print("PRODUCT DATA")
print(f"Name: {product1.name}")
print(f"Price: {product1.price:.2f}")
print(f"Discount percent: {product1.discountPercent:d}%")
print(f"Discount amount: {product1.getDiscountAmount():.2f}")
print(f"Discounted price: {product1.getDiscountPrice():.2f}")
