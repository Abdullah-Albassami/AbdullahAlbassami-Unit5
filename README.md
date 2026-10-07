# StockRoom

StockRoom is a Django catalogue and order data system focused on relational database design and Django ORM operations.

The project demonstrates models, migrations, CRUD operations, QuerySets, relationship traversal, constraints, annotation, and aggregation.

## Project Structure

```text
AbdullahAlbassami-Unit5/
├── ERD/
│   └── stockroom_erd.png
├── screenshots/
│   ├── CRUD.png
│   ├── QuerySets.png
│   ├── Relationships.png
│   ├── Aggregation_Annotation.png
│   ├── Constraints.png
│   └── Migrations.png
├── README.md
├── requirements.txt
└── stockroom_project/
    ├── manage.py
    ├── inventory/
    │   ├── admin.py
    │   ├── models.py
    │   ├── queries.py
    │   └── migrations/
    └── stockroom_project/
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
```

## Models

The project contains five main models:

- Category
- Product
- Customer
- Order
- OrderItem

## Relationships

- Category → Product: one-to-many
- Customer → Order: one-to-many
- Order → OrderItem: one-to-many
- Product → OrderItem: one-to-many
- Order ↔ Product: many-to-many through OrderItem

`OrderItem` is used as a through model because the relationship between an order and a product also stores:

- quantity
- unit_price

## Data Integrity

The project includes database constraints to ensure:

- Product SKU values are unique.
- Customer email addresses are unique.
- Product price cannot be negative.
- Product stock cannot be negative.
- OrderItem quantity must be at least 1.
- OrderItem unit price cannot be negative.
- The same product cannot appear twice in the same order.

## Migrations

The project includes:

1. An initial migration containing the main database structure.
2. A second migration that adds `Product.is_active`.

This demonstrates a deliberate schema change after the initial migration.

## Sample Data

The database contains:

- 3 categories
- 10 products
- 3 customers
- 5 orders
- 10 order items

The sample products include:

- Active products
- Inactive products
- Low-stock products
- Different price ranges

## CRUD Operations

CRUD operations are demonstrated in `inventory/queries.py`.

Examples include:

- Creating records
- Retrieving a record by primary key
- Listing records
- Updating product price and stock
- Deleting an unreferenced record

## QuerySet Operations

The project demonstrates:

- Filtering active products
- Filtering products with stock less than or equal to 5
- Filtering products within a price range
- Case-insensitive name searches
- Excluding inactive products
- Ordering by category and product name
- Returning the five most recent orders
- Searching with `Q` objects
- Using `F` expressions for database-side comparisons

## Relationship Traversal

Examples include:

- Product → Category
- Category → Products
- Customer → Orders
- Order → OrderItems
- OrderItem → Product
- Order → Products
- Product → Orders

### Forward Traversal

Forward traversal starts from the model containing the `ForeignKey` and accesses the related object directly.

Example:

```python
product.category
```

### Reverse Traversal

Reverse traversal starts from the referenced model and accesses related objects using `related_name`.

Example:

```python
category.products.all()
```

## Why OrderItem Is a Separate Model

`OrderItem` is used because the many-to-many relationship between `Order` and `Product` requires additional data.

Each relationship stores:

- `quantity`
- `unit_price`

This makes `OrderItem` a through model rather than using only Django's automatic many-to-many table.

## get() vs filter()

`get()` returns exactly one object and raises an exception if no object matches or if multiple objects match.

`filter()` returns a QuerySet containing zero, one, or many objects.

## Lazy QuerySets

Django QuerySets are lazy.

Creating a QuerySet normally does not immediately execute the database query. The query is evaluated when its results are actually needed, such as during iteration, conversion to a list, or displaying the results.

## Annotation and Aggregation

The project demonstrates:

- Total number of products using `Count`
- Average price of active products using `Avg`
- Total stock of active products using `Sum`
- Number of products per category using `annotate`
- Number of order items per order
- Total value of each order using quantity × unit price

### aggregate()

`aggregate()` calculates a summary for the entire QuerySet and returns one dictionary.

### annotate()

`annotate()` adds a calculated value to each returned object or group.

For category calculations, each `Category` is the group.

For order calculations, each `Order` is the group.

## Example Results

### Total Products

```text
10
```

### Average Active Product Price

```text
623.75
```

### Total Active Stock

```text
80
```

### Products per Category

```text
Electronics: 4
Clothing: 3
Food: 3
```

### Order Items per Order

```text
Order 1: 2
Order 2: 2
Order 3: 2
Order 4: 2
Order 5: 2
```

### Order Totals

```text
Order 1: 4000
Order 2: 1140
Order 3: 440
Order 4: 95
Order 5: 320
```

## Evidence Screenshots

The following screenshots demonstrate the required ORM operations and their returned results.

### CRUD Operations

![CRUD Operations](screenshots/CRUD.png)

### QuerySet Operations

![QuerySet Operations](screenshots/QuerySets.png)

### Relationship Traversal

![Relationship Traversal](screenshots/Relationships.png)

### Annotation and Aggregation

![Annotation and Aggregation](screenshots/Aggregation_Annotation.png)

### Constraints

![Constraints](screenshots/Constraints.png)

The screenshot demonstrates that the database-level check constraint rejects an invalid product with a negative price.

### Migrations

![Migrations](screenshots/Migrations.png)

The screenshot shows both inventory migrations applied successfully:

```text
0001_initial
0002_product_is_active
```

It also confirms that there are no pending migration operations.

## ERD

The project ERD is located at:

```text
ERD/stockroom_erd.png
```

![StockRoom ERD](ERD/stockroom_erd.png)

The ERD shows:

- Primary keys
- Foreign keys
- Cardinality
- Optionality
- The unique relationship constraint between `Order` and `Product` through `OrderItem`

## Setup

### 1. Create a virtual environment

From inside the Django project directory:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

From the repository root:

```bash
pip install -r requirements.txt
```

### 3. Move into the Django project

```bash
cd stockroom_project
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Check the project

```bash
python manage.py check
```

### 6. Run the development server

```bash
python manage.py runserver
```

## Known Limitations

- The project focuses mainly on the Django data layer.
- No advanced frontend interface was implemented.
- Sample data is manually created for ORM testing and demonstration.

## Future Improvements

Possible improvements include:

- Creating a full web interface
- Adding forms for catalogue and order management
- Adding user authentication
- Adding automated tests
- Adding search and filtering pages
- Adding reporting dashboards