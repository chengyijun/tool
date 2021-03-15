from views import router

if __name__ == "__main__":
    from fastapi import FastAPI
    import uvicorn

    app = FastAPI()
    app.include_router(router, prefix="/api")
    uvicorn.run(app=app)
