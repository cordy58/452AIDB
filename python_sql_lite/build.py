import os

from db import create_table, create_connection
from schema import *


def select_all_from_inventory(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_to_inventory(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
        INSERT INTO inventory VALUES
        (1, 'Kit-Kat', 1, 50),
        (2, 'Godiva', 1, 500),
        (3, 'Lindt', 1, 500),
        (4, 'Toblerone', 1, 250),
        (5, 'Gummy Bears', 2, 55),
        (6, 'Swedish Fish', 2, 55),
        (7, 'Gummy Worms', 2, 55),
        (8, 'Sour Gummy Worms', 2, 60),
        (9, 'Fruit Leather', 3, 60),
        (10, 'Goldfish', 3, 60),
        (11, 'Doritos', 3, 60),
        (12, 'Smarties', 3, 50);
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_category(conn):

    sql = """
        INSERT INTO category VALUES
	    (1, 'chocolate'),
        (2, 'gummy'),
        (3, 'other');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_customers(conn):

    sql = """
        INSERT INTO customer VALUES
	    (1, 'Mark', 'Lee','marklee@gmail.com'),
        (2, 'Johnny', 'Suh', 'suhjon@yahoo.com'),
        (3, 'Jennie', 'Kim', 'kenniejim@gmail.com'),
        (4, 'Jeno', 'Lee', 'lee123@bing.com'),
        (5, 'Karina', 'Yoo', 'karinayoo@gmail.com'),
        (6, 'Cordell', 'Thompson', 'cordy@gmail.com');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_employees(conn):
    sql = """
         INSERT INTO employee VALUES
	        (1, 'Nicolene', 'Jones','2020-09-01'),
            (2, 'Anna', 'Smith', '2021-12-01'),
            (3, 'Jessica', 'Brown', '2020-08-01');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_orders(conn):
    sql = """
        INSERT INTO orders VALUES
	    (1, 1, '2022-08-01', 1000, 2, 2, 1),
        (2, 4, '2022-08-01', 55, 5, 1, 3),
	    (3, 6, '2022-08-02', 5000, 3, 10, 2),
	    (4, 2, '2022-08-03', 50, 1, 1, 3),
	    (5, 4, '2022-08-04', 120, 11, 2, 2),
	    (6, 3, '2022-08-05', 50, 12, 1, 1),
	    (7, 1, '2022-08-05', 180, 10, 3, 3),
	    (8, 1, '2022-08-09', 300, 1, 6, 1),
	    (9, 1, '2022-08-13', 60, 8, 1, 2),
	    (10, 3, '2022-08-13', 500, 4, 2, 2),
	    (11, 5, '2022-08-13', 165, 5, 3, 1),
	    (12, 6, '2022-08-14', 10000, 3, 20, 3),
	    (13, 2, '2022-08-15', 55, 6, 1, 3),
	    (14, 3, '2022-08-15', 60, 9, 1, 2),
	    (15, 1, '2022-08-18', 55, 7, 1, 1),
	    (16, 2, '2022-08-20', 60, 8, 1, 2),
	    (17, 4, '2022-08-21', 180, 9, 3, 3),
	    (18, 4, '2022-08-25', 360, 9, 6, 3),
	    (19, 4, '2022-08-26', 720, 9, 12, 3),
	    (20, 1, '2022-08-29', 500, 2, 1, 2);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_category_table)
    insert_to_category(conn)
    create_table(conn, sql_create_inventory_table)
    insert_to_inventory(conn)
    create_table(conn, sql_create_customer_table)
    insert_to_customers(conn)
    create_table(conn, sql_create_employee_table)
    insert_to_employees(conn)
    create_table(conn, sql_create_orders_table)
    insert_to_orders(conn)

    print("Database build successful!")

if __name__ == "__main__":
    main()