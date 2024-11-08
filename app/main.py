import os
from aiohttp import web
from .db import create_pool
from .tasks import get_tasks, create_task


async def init_app():
    app = web.Application()

    app['db_pool'] = await create_pool()

    app.router.add_get('/tasks', get_tasks)
    app.router.add_post('/tasks', create_task)

    return app

if __name__ == '__main__':
    web.run_app(init_app(), port=int(os.getenv('PORT', 8000)))
