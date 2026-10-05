import sqlite3
from datetime import time


# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('restaurant.db')

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

# SQL queries to create the table
menu_creation_query = """
	CREATE TABLE menu_items (
		menu_item int PRIMARY KEY,
		item_name varchar(255),
		category varchar(255),
		price decimal(4,2)
	)
"""
orders_creation_query = """
	CREATE TABLE order_details (
		order_details_id int PRIMARY KEY,
		order_id int,
		order_date date,
		order_time time,
		item_id int
	)
"""

# Execute the table creation queries
cursor_obj.execute(menu_creation_query)
connection_obj.commit()
cursor_obj.execute(orders_creation_query)
connection_obj.commit()

# Read the csv files and insert the data into the new tables
with open('menu_items.csv', 'r') as f:
	next(f)
	for line in f:
		data = line.split(",")
		cursor_obj.execute(f"INSERT INTO menu_items (menu_item, item_name, category, price) VALUES ({data[0]}, '{data[1]}', '{data[2]}', {data[3]})")
		connection_obj.commit()
with open('order_details.csv', 'r') as ff:
	next(ff)
	for line in ff:
		data = line.split(",")
		temp = data[3].split(" ") #split into TIME and AM/PM
		other = temp[0].split(":")
		if temp[1] == "PM":
			other[0] = str(int(other[0]) + 12)
		data[3] = str(other[0] + ":" + other[1] + ":" + other[2])
		cursor_obj.execute(f"INSERT INTO order_details (order_details_id, order_id, order_date, order_time, item_id) VALUES ({data[0]}, {data[1]}, '{data[2]}', '{data[3]}', {data[4]})")
		connection_obj.commit()

# Close the connection to the database
cursor_obj.close()
connection_obj.close()
