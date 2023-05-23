from pydantic import BaseModel

class struct_item(BaseModel):
    # id : int
    title : str
    content : str
