Django E-Commerce Admin Interface and Data Model

This project is a production-grade Django backend for managing an e-commerce store, offering a robust data model and a customizable admin interface to handle various operations related to products, orders, customers, and more.
Features

    Admin Interface: A powerful, user-friendly interface for managing products, collections, customers, and orders.
    Product Management: Add, update, and remove products. Manage inventory, pricing, and featured items.
    Customer Management: Handle customer details, including membership status, order history, and personal information.
    Order Management: Track and process customer orders with detailed information on order items, quantities, and prices.
    Data Model: A well-structured and scalable database schema optimized for e-commerce operations.

Data Model Overview
1. Product

    Represents the items available for sale.
    Key fields: title, description, price, inventory, and featured product status.

2. Collection

    Grouping of products for display in the store.
    Key fields: name, description, featured product.

3. Customer

    Represents customers using the platform.
    Key fields: first name, last name, email, membership status, and address.

4. Order

    Tracks customer purchases.
    Key fields: customer, order date, status, total price.

5. OrderItem

    Represents individual items within an order.
    Key fields: product, quantity, unit price.

Admin Interface

The admin panel allows store administrators to:

    Add, edit, and delete products.
    Manage product collections.
    View and manage customer details and their orders.
    Track inventory levels and featured products.
    View detailed reports on orders, sales, and customers.

The interface provides an intuitive way to interact with the data model, making it easy to manage the store's backend.

Clone
git clone https://github.com/eugenius-watchman/django.git


 
