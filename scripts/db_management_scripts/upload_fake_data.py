import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from config import config
import os

async def main():
    db_host = config.DB_HOST
    db_port = config.DB_PORT

    if os.getenv('STAGE') == 'development':
        mongo_uri = f'mongodb://{db_host}:{db_port}'
    else:
        db_name = config.DB_NAME
        db_user = config.DB_USER
        db_pass = config.DB_PASS
        mongo_uri = f'mongodb://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

    client = AsyncIOMotorClient(mongo_uri)
    db = client['FakeFit']

    try:
        await client.admin.command('ping')
        print('Connected to MongoDB')
    except Exception as e:
        print(f'Error: {e}')


 


if __name__ == "__main__":
    asyncio.run(main())


