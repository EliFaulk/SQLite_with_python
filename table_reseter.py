import sqlite3

connection_obj = sqlite3.connect('restaurant.db')
cursor_obj = connection_obj.cursor()

cursor_obj.execute("""DROP TABLE IF EXISTS menu_items""")
cursor_obj.execute("""DROP TABLE IF EXISTS order_details""")

connection_obj.close()
