sql_create_category_table = """
    CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category_name TEXT
    );
"""

sql_create_inventory_table = """
    CREATE TABLE inventory (
        item_id INT PRIMARY KEY ,
        item_name TEXT,
        category_id INT,
        unit_price REAL,
        FOREIGN KEY (category_id) references category(category_id) ON UPDATE CASCADE ON DELETE CASCADE
    );
"""

sql_create_customer_table = """
    CREATE TABLE customer (
    customer_id INT PRIMARY KEY ,
    first_name TEXT,
    last_name TEXT,
    email TEXT
);
"""

sql_create_employee_table = """
    CREATE TABLE employee (
        emp_id INT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        hire_date TEXT);
"""

sql_create_orders_table = """
    CREATE TABLE orders(
        order_id INT PRIMARY KEY,
        customer_id INT,
        order_date DATETIME,
        total_price REAL,
        item_id INT,
        quantity INT DEFAULT 0,
        emp_id INT,
        FOREIGN KEY (item_id) references inventory(item_id)
        FOREIGN KEY (customer_id) references customers(customer_id)
        FOREIGN KEY (emp_id) references employee(emp_id)
    );
"""

def get_schema():
    schema = f"{sql_create_category_table}{sql_create_inventory_table}{sql_create_customer_table}{sql_create_employee_table}{sql_create_orders_table}"
    return schema