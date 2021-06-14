from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/products", response_model=List[schemas.Product])
async def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@app.get("/product/{name}", response_model=schemas.Product)
async def get_product(name: str, db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.name == name).first()

@app.post("/product", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return db_product

# @app.on_event("startup")
# async def startup():
#     await database.connect()
# 
# 
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()