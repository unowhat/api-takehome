-- USAGE: In psql CLI, execute \i queries/seed_tables.sql

-- seeding departments
INSERT INTO departments (department_name) VALUES ('Bakery'), ('Produce');

--seeding categories
INSERT INTO categories (category_name, department_id) 
    SELECT 'Bread', department_id FROM departments WHERE department_name='Bakery';

INSERT INTO categories (category_name, department_id) 
    SELECT 'Cookies', department_id FROM departments WHERE department_name='Bakery';

INSERT INTO categories (category_name, department_id) 
    SELECT 'Fruits', department_id FROM departments WHERE department_name='Produce';

INSERT INTO categories (category_name, department_id) 
    SELECT 'Vegetables', department_id FROM departments WHERE department_name='Produce';

--seeding products
INSERT INTO products (product_name, category_id, price) 
    SELECT 'Wheat Bread', category_id, 2.00 FROM categories WHERE category_name='Bread';
INSERT INTO products (product_name, category_id, price) 
    SELECT 'Rye Bread', category_id, 3.10 FROM categories WHERE category_name='Bread';

INSERT INTO products (product_name, category_id, price) 
    SELECT 'Sugar Cookies', category_id, 1.50 FROM categories WHERE category_name='Cookies';
INSERT INTO products (product_name, category_id, price) 
    SELECT 'Oatmeal Cookies', category_id, 2.10 FROM categories WHERE category_name='Cookies';
INSERT INTO products (product_name, category_id, price) 
    SELECT 'Chocolate Chip Cookies', category_id, 2.30 FROM categories WHERE category_name='Cookies';

INSERT INTO products (product_name, category_id, price) 
    SELECT 'Apples', category_id, 2.20 FROM categories WHERE category_name='Fruits';
INSERT INTO products (product_name, category_id, price) 
    SELECT 'Oranges', category_id, 3.10 FROM categories WHERE category_name='Fruits';

INSERT INTO products (product_name, category_id, price) 
    SELECT 'Celery', category_id, 1.60 FROM categories WHERE category_name='Vegetables';