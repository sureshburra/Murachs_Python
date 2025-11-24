from objects import Product
from custom_logger import CustomLogger

logger = CustomLogger().get_logger()

product1 = Product("Stanley Hammer", 12.99, 62)
product2 = Product("National Hardware", 5.06, 0)

print("PRODUCT DATA")
print(f"Name: {product1.name}")
print(f"Price: {product1.price:.2f}")
print(f"Discount percent: {product1.discountPercent:d}%")
print(f"Discount amount: {product1.getDiscountAmount():.2f}")
print(f"Discounted price: {product1.getDiscountPrice():.2f}")

logger.info("Product data")
logger.info(f"Name: {product1.name}")
logger.info(f"Price: {product1.price:.2f}")
logger.info(f"Discount percent: {product1.discountPercent:d}%")
logger.info(f"Discount amount: {product1.getDiscountAmount():.2f}")
logger.info(f"Discounted price: {product1.getDiscountPrice():.2f}")

logger.error("This is an error message")

