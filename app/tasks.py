from aiohttp import web
from .db import create_pool
from .models import Task


async def get_tasks(request):
    pool = request.app['db_pool']
    async with pool.acquire() as conn:
        tasks = await conn.fetch("SELECT * FROM tasks")
        return web.json_response([dict(task) for task in tasks])


async def create_task(request):
    pool = request.app['db_pool']
    data = await request.json()
    task = Task(**data)

    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO tasks (title, description, status) VALUES ($1, $2, $3)",
                           task.title, task.description, task.status)

    return web.json_response(task.dict(), status=201)
