from django.core.management.base import BaseCommand
from django.db import transaction

from inventory.models import Category, Product, Customer, Order, OrderItem


class Command(BaseCommand):
    help = "Create the StockRoom sample data used for the project."

    @transaction.atomic
    def handle(self, *args, **options):

        # Clear existing inventory data so the command can be run repeatedly.
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        Category.objects.all().delete()

        # Categories
        electronics = Category.objects.create(name="Electronics")
        clothing = Category.objects.create(name="Clothing")
        food = Category.objects.create(name="Food")

        # Products
        laptop = Product.objects.create(
            name="Laptop",
            sku="ELEC-001",
            price=3400.00,
            stock=8,
            is_active=True,
            category=electronics,
        )

        keyboard = Product.objects.create(
            name="Keyboard",
            sku="ELEC-002",
            price=250.00,
            stock=5,
            is_active=True,
            category=electronics,
        )

        mouse = Product.objects.create(
            name="Mouse",
            sku="ELEC-003",
            price=120.00,
            stock=0,
            is_active=False,
            category=electronics,
        )

        monitor = Product.objects.create(
            name="Monitor",
            sku="ELEC-004",
            price=900.00,
            stock=7,
            is_active=True,
            category=electronics,
        )

        shirt = Product.objects.create(
            name="T-Shirt",
            sku="CLOTH-001",
            price=80.00,
            stock=20,
            is_active=True,
            category=clothing,
        )

        jacket = Product.objects.create(
            name="Jacket",
            sku="CLOTH-002",
            price=300.00,
            stock=3,
            is_active=True,
            category=clothing,
        )

        Product.objects.create(
            name="Jeans",
            sku="CLOTH-003",
            price=180.00,
            stock=12,
            is_active=False,
            category=clothing,
        )

        coffee = Product.objects.create(
            name="Coffee",
            sku="FOOD-001",
            price=35.00,
            stock=30,
            is_active=True,
            category=food,
        )

        chocolate = Product.objects.create(
            name="Chocolate",
            sku="FOOD-002",
            price=15.00,
            stock=5,
            is_active=True,
            category=food,
        )

        biscuits = Product.objects.create(
            name="Biscuits",
            sku="FOOD-003",
            price=10.00,
            stock=2,
            is_active=True,
            category=food,
        )

        # Customers
        customer1 = Customer.objects.create(
            name="Ahmed Ali",
            email="ahmed@example.com",
        )

        customer2 = Customer.objects.create(
            name="Sara Mohammed",
            email="sara@example.com",
        )

        customer3 = Customer.objects.create(
            name="Khalid Hassan",
            email="khalid@example.com",
        )

        # Orders
        order1 = Order.objects.create(
            customer=customer1,
            status=Order.Status.PENDING,
        )

        order2 = Order.objects.create(
            customer=customer1,
            status=Order.Status.COMPLETED,
        )

        order3 = Order.objects.create(
            customer=customer2,
            status=Order.Status.PROCESSING,
        )

        order4 = Order.objects.create(
            customer=customer3,
            status=Order.Status.COMPLETED,
        )

        order5 = Order.objects.create(
            customer=customer3,
            status=Order.Status.CANCELLED,
        )

        # Order items
        OrderItem.objects.create(
            order=order1,
            product=laptop,
            quantity=1,
            unit_price=3500.00,
        )

        OrderItem.objects.create(
            order=order1,
            product=keyboard,
            quantity=2,
            unit_price=250.00,
        )

        OrderItem.objects.create(
            order=order2,
            product=monitor,
            quantity=1,
            unit_price=900.00,
        )

        OrderItem.objects.create(
            order=order2,
            product=shirt,
            quantity=3,
            unit_price=80.00,
        )

        OrderItem.objects.create(
            order=order3,
            product=jacket,
            quantity=1,
            unit_price=300.00,
        )

        OrderItem.objects.create(
            order=order3,
            product=coffee,
            quantity=4,
            unit_price=35.00,
        )

        OrderItem.objects.create(
            order=order4,
            product=chocolate,
            quantity=5,
            unit_price=15.00,
        )

        OrderItem.objects.create(
            order=order4,
            product=biscuits,
            quantity=2,
            unit_price=10.00,
        )

        OrderItem.objects.create(
            order=order5,
            product=keyboard,
            quantity=1,
            unit_price=250.00,
        )

        OrderItem.objects.create(
            order=order5,
            product=coffee,
            quantity=2,
            unit_price=35.00,
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Sample data created: "
                "3 categories, 10 products, 3 customers, "
                "5 orders, and 10 order items."
            )
        )