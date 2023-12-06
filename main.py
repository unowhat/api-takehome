from fastapi import FastAPI
# from products import get_all_products
# from sqlalchemy import create_engine, select
# from sqlalchemy.orm import sessionmaker
from databases import Database

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
async def get_products(department_id: int):
    query = '''SELECT department_name, AVG(price) AS average_price 
        FROM products AS p LEFT JOIN categories AS c ON p.category_id=c.category_id 
        LEFT JOIN departments AS d ON c.department_id=d.department_id
        WHERE c.department_id=:department_id 
        GROUP BY d.department_name'''
    
    rows = await database.fetch_one(query=query, values={'department_id':department_id})
    return rows