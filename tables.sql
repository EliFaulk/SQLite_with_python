CREATE TABLE menu_items (
menu_items int PRIMARY KEY,
item_name varchar(255),
category varchar(255),
price decimal(4,2)
);
CREATE TABLE order_details (
order_details_id int PRIMARY KEY,
order_id int,
order_date varchar(255),
order_time varchar(255),
item_id int
);
