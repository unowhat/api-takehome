### What problems did you encounter?
1. Technology choice for connecting psql db with the main server
2. FastAPI basic syntax 

### How did you solve them? 
1. I used [databases](https://www.encode.io/databases/) library as the tool to execute queries from servers
2. I mainly consulted [FastAPI](https://fastapi.tiangolo.com/tutorial/) documentations for answers

### What design tradeoffs did you make? 
Due to the limitation of time, I did some tradeoffs on the package structure, for example:
   - All routes are in the same file
   - Models are implemented to the minimum
   - All SQL queries are RAW
   - No unit tests, all tests were conducted through Postman on end-to-end behaviors

### Given more time how could you improve your project (improve its performance, make it more usable, maintainable, testable, etc.)?
- Using query builders instead of using RAW SQL queries
- Re-structure the routes and services into different modules to make it more maintainable
- Writing unit tests; testing codes throughly
- Implementing CRUD for 'departments'