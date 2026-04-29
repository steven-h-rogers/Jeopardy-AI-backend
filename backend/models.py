from pydantic import BaseModel

class CategoryPayload(BaseModel):
    num_categories: int = 6 # if missing -> 6, if a different int -> that int
    custom_categories: list[str]|None = None

class PointPayload(BaseModel):
    point_map: list[list[int]] | list[int] | None = None

