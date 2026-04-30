from pydantic import BaseModel

class CategoryPayload(BaseModel):
    num_categories: int = 6 # if missing -> 6, if a different int -> that int
    # use_classic_categories: bool = False
    

# future model for custom point layout
# class PointPayload(BaseModel):
#     point_map: list[list[int]] | list[int] | None = None

