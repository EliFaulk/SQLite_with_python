import sqlite3
from datetime import time


class Order:
        def __init__(self, order_details_id, order_id, order_date, order_time, item_id):
                self.order_details_id = order_details_id
                self.order_id = order_id
                self.order_date = order_date
                self.order_time = order_time
                self.item_id = item_id

        def __str__(self):
                return f"({self.order_details_id}, {self.order_id}, '{self.order_date}', '{self.order_time}', {self.item_id})"

class MenuItem:
        def __init__(self, menu_item, item_name, category, price):
                self.menu_item = menu_item
                self.item_name = item_name
                self.category = category
                self.price = price

        def __str__(self):
                return f"({self.menu_item}, '{self.item_name}', '{self.category}', {self.price})"


# Connect to the SQLite database
connection_obj = sqlite3.connect('restaurant.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()


# CALCULATIONS
# All items with a price over $10
print(" = = = = ITEMS WITH PRICE > $10 = = = = ")
cursor_obj.execute('''SELECT * FROM menu_items WHERE price > 10.0''')
output = cursor_obj.fetchall()
for row in output:
	print(row)

# Items listed in order from earliest order in the day to latest
print(" = = = = ORDERS SORTED BY TIME = = = = ")
cursor_obj.execute('''SELECT * FROM order_details ORDER BY order_time''')
output = cursor_obj.fetchall()
print("Remove comment from print statement to see all orders")
#for row in output:
#	print(row)

# Count orange chicken orders
print(" = = = = COUNT OF ORANGE CHICKEN ORDERS = = = = ")
cursor_obj.execute('''SELECT COUNT(*) FROM order_details INNER JOIN menu_items ON order_details.item_id = menu_items.menu_item WHERE item_name = "Orange Chicken"''')
output = cursor_obj.fetchall()
print(output)

# Total cost of items purchased after 9 PM
print(" = = = = TOTAL COST OF ITEMS ORDERED AFTER 9 PM = = = = ")
cursor_obj.execute('''SELECT SUM(price) FROM menu_items INNER JOIN order_details ON order_details.item_id = menu_items.menu_item WHERE order_time > "21:00:00"''')
output = cursor_obj.fetchall()
print(output)

# Create lists of table contents using SELECT
menu = []
orders = []
cursor_obj.execute('''SELECT * FROM menu_items''')
output = cursor_obj.fetchall()
for row in output:
	menu.append(MenuItem(row[0], row[1], row[2], row[3]))
cursor_obj.execute('''SELECT * FROM order_details''')
output = cursor_obj.fetchall()
for row in output:
	orders.append(Order(row[0], row[1], row[2], row[3], row[4]))

# Repeated calculations with Python
print(" = = = = ITEMS WITH PRICE > $10 = = = =  PYTHON")
for item in menu:
	if item.price > 10.0:
		print(item)

print(" = = = = ORDERS SORTED BY TIME = = = =  PYTHON")
sorted_orders = sorted(orders, key=lambda ord: ord.order_time)
print("Remove comment to print full printed list of orders sorted by time")
#for order in sorted_orders:
#	print(order)

print(" = = = = COUNT OF ORANGE CHICKEN ORDERS = = = =  PYTHON")
orange_chicken = 0
orange_chicken_count = 0
for item in menu:
	if item.item_name == "Orange Chicken":
		orange_chicken = item.menu_item
		break
for order in orders:
	if order.item_id == orange_chicken:
		orange_chicken_count += 1
print(orange_chicken_count)

print(" = = = = TOTAL COST OF ITEMS ORDERED AFTER 9 PM = = = =  PYTHON")
total_cost = 0;
for order in orders:
	if order.order_time > "21:00:00":
		for item in menu:
			if item.menu_item == order.item_id:
				total_cost += item.price
print(round(total_cost, 2))


cursor_obj.close()
connection_obj.close()
