# activity_db.py
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from enum import Enum
from activity import ActivityCreate, Priority, Interval  # Import ActivityCreate and Enums from activity.py
from typing import Optional

class Status(str, Enum):
    pending = "pending"
    completed = "completed"
    cancelled = "cancelled"

# Activity DB Model (for database storage)
class ActivityDB(ActivityCreate):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: Status = Field(default=Status.pending)
    due_date: Optional[datetime] = None
    completed: bool = Field(default=False)
    user_id: Optional[str] = None  # or UUID depending on your use case
    deleted: bool = Field(default=False)
    visibility: Optional[str] = Field(default="private")  # can be "private" or "public"

    # Auto-update `updated_at` before update (could be handled in database)
    @field_validator("updated_at", mode="before")
    def set_updated_at(cls, v):
        # Always set the updated_at to the current UTC time if it's not provided
        return datetime.now(timezone.utc) if v is None else v
