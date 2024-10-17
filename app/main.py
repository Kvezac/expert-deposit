import uvicorn
from fastapi import FastAPI, APIRouter


def create_app():
    app = FastAPI(
        debug=True,
        docs_url='/api/docs',
        title='Deposit Calculate v15'
    )
    app.include_router(ping_router)
    return app


ping_router = APIRouter(prefix='/ping', tags=['ping app and db'])


@ping_router.get('/app')
def ping_app():
    return {'text': 'App is working'}


if __name__ == '__main__':
    uvicorn.run(app='main:create_app', factory=True, host='localhost', port=8000)
