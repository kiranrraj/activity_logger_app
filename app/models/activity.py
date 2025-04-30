from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from enum import Enum

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"
    urgent = "urgent"
    optional = "optional"

class Interval(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"

class ActivityCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=100, examples="My Title")
    priority: Priority = Field(...,examples="High")
    repeat: bool = Field(..., examples=False)
    interval: Interval = Field(None, examples="Daily")
    description: Optional[str] = Field(..., min_length=2, max_length=300, examples="Description")
    sub_tasks: Optional[List[str]] = Field(default_factory=list)
    tags: Optional[List[str]] = Field(default_factory=list) 

    @field_validator("tags", pre=True)
    def validator_tags(cls, value):
        if value and len(value) >10:
            raise ValueError("Tag has a maximum of 10 tags")
        for tag in value:
            if len(tag) > 30:
                raise ValueError("Each tag have a maximum of 30 character")
            if not tag.islower():
                raise ValueError("Tags should be in lower case and contains no spaces")
        return value
    
    @field_validator("title", "description", pre=True)
    def strip_whitespace(cls, value):
        return value.strip()
        