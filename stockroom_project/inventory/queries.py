from django.db.models import Q, F, Count, Sum, Avg, DecimalField, ExpressionWrapper

from .models import Category, Product, Customer, Order, OrderItem

# CRUD OPERATIONS


def create_example_category():
    return Category.objects.create(name="Example")


def retrieve_product(pk):
    return Product.objects.get(pk=pk)


def list_products():
    return Product.objects.all()[:5]


def update_product(pk, price, stock):
    product = Product.objects.get(pk=pk)
    product.price = price
    product.stock = stock
    product.save()
    return product


def delete_category(pk):
    category = Category.objects.get(pk=pk)
    return category.delete()

# QUERYSET OPERATIONS


def get_active_products():
    return Product.objects.filter(is_active=True)


def get_low_stock_products():
    return Product.objects.filter(stock__lte=5)


def get_products_in_price_range(min_price, max_price):
    return Product.objects.filter(price__range=(min_price, max_price))


def search_products_by_name(search):
    return Product.objects.filter(name__icontains=search)


def get_products_excluding_inactive():
    return Product.objects.exclude(is_active=False)


def get_products_ordered():
    return Product.objects.order_by("category__name", "name")


def get_recent_orders():
    return Order.objects.order_by("-created_at")[:5]


def search_products_by_name_or_sku(search):
    return Product.objects.filter(
        Q(name__icontains=search) |
        Q(sku__icontains=search)
    )


def increment_product_stock(sku, amount=1):
    return Product.objects.filter(sku=sku).update(
        stock=F("stock") + amount
    )

# RELATIONSHIP QUERIES


def get_product_category(sku):
    product = Product.objects.get(sku=sku)
    return product.category


def get_category_products(category_name):
    category = Category.objects.get(name=category_name)
    return category.products.all()


def get_customer_orders(email):
    customer = Customer.objects.get(email=email)
    return customer.orders.all()


def get_order_items(order_id):
    order = Order.objects.get(pk=order_id)
    return order.items.all()


def get_order_item_product(order_item_id):
    item = OrderItem.objects.get(pk=order_item_id)
    return item.product


def get_order_products(order_id):
    order = Order.objects.get(pk=order_id)
    return order.products.all()


def get_product_orders(sku):
    product = Product.objects.get(sku=sku)
    return product.orders.all()

# ANNOTATION AND AGGREGATION


def get_total_product_count():
    return Product.objects.aggregate(
        total_products=Count("id")
    )


def get_average_active_product_price():
    return Product.objects.filter(is_active=True).aggregate(
        average_price=Avg("price")
    )


def get_total_active_stock():
    return Product.objects.filter(is_active=True).aggregate(
        total_stock=Sum("stock")
    )


def get_product_count_by_category():
    return Category.objects.annotate(
        product_count=Count("products")
    ).values("name", "product_count")


def get_order_item_count_by_order():
    return Order.objects.annotate(
        item_count=Count("items")
    ).values("id", "item_count")


def get_order_totals():
    return Order.objects.annotate(
        total_value=Sum(
            ExpressionWrapper(
                F("items__quantity") * F("items__unit_price"),
                output_field=DecimalField(
                    max_digits=12,
                    decimal_places=2
                ),
            )
        )
    ).values("id", "total_value")


# REQUIRED EXPLANATIONS

# Forward relationship traversal:
# Starts from the model containing the ForeignKey and accesses
# the related object directly.
# Example: product.category


# Reverse relationship traversal:
# Starts from the referenced model and accesses objects that point
# to it using the related_name.
# Example: category.products.all()


# Why OrderItem is a separate model:
# Order and Product have a many-to-many relationship, but the
# relationship also needs quantity and unit_price. OrderItem acts
# as the through model and stores this additional relationship data.


# get() vs filter():
# get() returns one object and raises an exception if no matching
# object exists or if multiple objects match.
# filter() returns a QuerySet containing zero, one, or many objects.


# Lazy QuerySets:
# Django QuerySets are lazy because creating a QuerySet normally
# does not execute the SQL query immediately. The query is evaluated
# when its results are actually needed, such as during iteration,
# conversion to a list, or displaying the results.


# aggregate() vs annotate():
# aggregate() calculates a summary for the whole QuerySet and
# returns a single dictionary.
#
# annotate() adds a calculated value to each returned object or group.


# GROUPING EXPLANATION
# When Category objects are annotated with Count("products"),
# each Category is the group.
#
# When Order objects are annotated with Count("items") or a total
# value, each Order is the group.