from dotenv import load_dotenv
# Load the .env file
load_dotenv()

# Now you can access the variables
import os
db_uri = os.getenv('DATABASE_URI')
api_key = os.getenv('API_KEY')

from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(todo_router)
register_tortoise(
    app=app, 
    config={
      'connections': {
          'default': {
              'engine': 'tortoise.backends.asyncpg',
              'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'dev',
                'password': 'dev',
                'database': 'rag',
              }
          },
      },
      'apps': {
          'models': {
              'models': ['api.models.todo'],
              'default_connection': 'default',
          }
      }
    },
    add_exception_handlers=True,
    generate_schemas=True,
    # modules={"models":["api.models.todo"]}
)

@app.get("/")
def index():
    return {"status":"todo api is running"}
