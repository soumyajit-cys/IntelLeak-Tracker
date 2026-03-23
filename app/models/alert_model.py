from pydantic import BaseModel

class Alert(BaseModel):
    keyword: str
    matched_data: dict


    