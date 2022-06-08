from home.models import Product
#1. Inserting new record
product1 = Product(product_name="LV bag", product_price="3000", product_cat="bags")
product1.save()

#2. getting all records in product table
Product.objects.all()

#3. filtering products by name
Product.objects.filter(product_name="Lv bag")

#4. getting single record from the product table
Product.objects.filter(product_name="LV bag").first()

#5. Changing a product price
product1.product_price="2000"
product1.save()