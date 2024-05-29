from pydantic import BaseModel
from enum import Enum
from typing import Annotated



class Suffix(str, Enum):
    currency = "c"
    percentage = "p"

class TypeLabel(str, Enum):
    str = "str"
    int = "int"
    float = "float"
    bool = "bool"

class LabelText(BaseModel):
    label: str | None = "N/A"
    dtype: TypeLabel | None
    value: str | int | float | bool | None = "N/A"
    prefix: Suffix | None = None

class StockData(BaseModel):
    current_price: LabelText
    market_cap: LabelText
    name: LabelText
    site_name: LabelText
    country: LabelText
    sector: LabelText
    industry: LabelText
    book_value: LabelText
    dividend_rate: LabelText
    dividend_yield: LabelText
    quote_type: LabelText
    yield_etf: LabelText
