from fastapi import FastAPI

from src.core.config import settings
from src.api.books import router as book_router


def create_app() -> FastAPI:
    app = FastAPI(title="itinerarios", debug=settings.DEBUG)
    app.include_router(book_router)
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
