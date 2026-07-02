from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime


# ─────────────────────────────────────────────
# 1. Enums — restrict values to a fixed set
# ─────────────────────────────────────────────
class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Category(str, Enum):
    work = "work"
    personal = "personal"
    shopping = "shopping"
    other = "other"


# ─────────────────────────────────────────────
# 2. BASE schema — common fields
# ─────────────────────────────────────────────
class TaskBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    title: str = Field(
        ...,                          # `...` means REQUIRED
        min_length=3,
        max_length=100,
        examples=["Buy groceries"],   # Shows up in /docs
        description="The task title"
    )
    description: Optional[str] = Field(
        None,                        # Optional, defaults to None
        max_length=500,
        examples=["Milk, eggs, bread"]
    )
    priority: Priority = Field(
        default=Priority.medium,      # Default value
        examples=["high"]
    )
    category: Category = Field(
        default=Category.personal,
        examples=["shopping"]
    )
    due_date: Optional[datetime] = Field(
        None,
        examples=["2026-12-31T23:59:00"]
    )


# ─────────────────────────────────────────────
# 3. CREATE — what the client SENDS
# ─────────────────────────────────────────────
class TaskCreate(TaskBase):
    # Inherits all fields from TaskBase
    # Add create-specific fields here if needed
    pass


# ─────────────────────────────────────────────
# 4. UPDATE — partial updates allowed
# ─────────────────────────────────────────────
class TaskUpdate(BaseModel):
    # Every field is Optional for partial updates
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Optional[Priority] = None
    category: Optional[Category] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None


# ─────────────────────────────────────────────
# 5. RESPONSE — what the API RETURNS
# ─────────────────────────────────────────────
class Task(TaskBase):
    id: int
    completed: bool = False
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
