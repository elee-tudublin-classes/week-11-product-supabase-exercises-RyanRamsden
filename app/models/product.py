# A model class for Product items
# See https://docs.pydantic.dev/latest/concepts/models/

from pydantic import BaseModel, validator
from typing import Optional

class Product(BaseModel):
    _id: int # Pydantic excludes variables which begin with an underscore. 
    category_id: int
    title: str
    description: str
    price: float
    stock: int
    thumbnail: str = ""

    # https://docs.pydantic.dev/latest/concepts/validators/
    # if thumbnail missing, use a default
    @validator('thumbnail')
    def default_image(cls, v):
        assert v is not None, 'thumbnail image not supplied, using placeholder'
        if (v == "") :
            return("/static/images/product/placeholder.webp")
        return v