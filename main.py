from fastapi import FastAPI
from databases import Database

from models.product import Product
from models.category import Category
from models.department import Department

app = FastAPI()

DATABASE_URL = "postgresql://demouser:password123@db:5432/demo"

database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/products")
async def get_products():
    query = 'SELECT product_name AS product, price FROM products'
    rows = await database.fetch_all(query=query)
    return rows

@app.get("/category/{department_id}/avg-price")
async def get_department_average_price(department_id: int):
    query = '''SELECT department_name, AVG(price) AS average_price 
        FROM products AS p LEFT JOIN categories AS c ON p.category_id=c.category_id 
        LEFT JOIN departments AS d ON c.department_id=d.department_id
        WHERE c.department_id=:department_id 
        GROUP BY d.department_name'''
    
    rows = await database.fetch_one(query=query, values={'department_id':department_id})
    return rows

@app.post("/product/")
async def create_product(product: Product):
    query = '''INSERT INTO products (product_name, category_id, price) 
         SELECT :product_name, category_id, :price FROM categories WHERE category_name=:category_name;'''
    
    await database.execute(
        query=query, 
        values={
            'product_name': product.name, 
            'category_name': product.category, 
            'price': product.price
        }
    )

    return "Success"

@app.get("/product/{product_name}")
async def get_product(product_name: str):
    query = '''SELECT p.product_id, p.product_name, c.category_name, p.price 
        FROM products AS p LEFT JOIN categories AS c ON p.category_id=c.category_id  
        WHERE p.product_name=:product_name;'''
    
    rows = await database.fetch_one(
        query=query, 
        values={
            'product_name': product_name, 
        }
    )

    return rows

@app.put("/product/{product_id}")
async def update_product(product_id: int, product: Product):
    category_id_query = '''SELECT category_id FROM categories WHERE category_name=:category_name'''
    category_id_rows = await database.fetch_one(
        query=category_id_query, 
        values={
            'category_name': product.category, 
        }
    )

    query = '''UPDATE products
        SET product_name=:product_name, category_id=:category_id, price=:price 
        WHERE product_id=:product_id;'''
    
    await database.execute(
        query=query, 
        values={
            'product_name': product.name, 
            'category_id': category_id_rows['category_id'], 
            'price': product.price,
            'product_id': product_id
        }
    )

    return "Success"

@app.delete("/product/{product_id}")
async def delete_products(product_id: int):
    query = 'DELETE FROM products WHERE product_id=:product_id;'
    
    await database.execute(
        query=query, 
        values={
            'product_id': product_id, 
        }
    )

    return "Success"

@app.post("/category/")
async def create_category(category: Category):
    query = '''INSERT INTO categories (category_name, department_id) 
        SELECT :category_name, department_id FROM departments WHERE department_name=:department_name;'''
    
    await database.execute(
        query=query, 
        values={
            'category_name': category.name, 
            'department_name': category.department
        }
    )

    return "Success"

@app.get("/category/{category_id}")
async def get_category(category_id: int):
    query = ''' SELECT c.category_id, c.category_name, d.department_id, d.department_name
        FROM categories AS c LEFT JOIN departments AS d ON c.department_id=d.department_id 
        WHERE category_id=:category_id;'''
    
    rows = await database.fetch_one(
        query=query, 
        values={
            'category_id': category_id
        }
    )

    return rows

@app.put("/category/{category_id}")
async def update_category(category_id: int, category: Category):
    department_id_query = 'SELECT department_id FROM departments WHERE department_name=:department_name'
    rows = await database.fetch_one(
        query=department_id_query,
        values={
            'department_name': category.department 
        }
    )

    query = ''' UPDATE categories
        SET category_name=:category_name, department_id=:department_id
        WHERE category_id=:category_id;'''
    
    await database.execute(
        query=query, 
        values={
            'category_id': category_id,
            'category_name': category.name,
            'department_id': rows['department_id']
        }
    )

    return 'Success'

@app.delete("/category/{category_id}")
async def delete_category(category_id: int):
    query = 'DELETE FROM categories WHERE category_id=:category_id;'
    
    await database.execute(
        query=query, 
        values={
            'category_id': category_id
        }
    )

    return 'Success'