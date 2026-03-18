from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.router.product import router as product_router
from app.router.category import router as category_router
from fastapi_pagination import add_pagination


app = FastAPI(title="UZUMDB", docs_url="/")

app.include_router(category_router)
app.include_router(product_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def read_root():
    return FileResponse("frontend/salom.html")
add_pagination(app)