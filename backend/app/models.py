from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
import uuid


class User(SQLModel, table=True):
    """User model for authentication and task ownership."""
    __tablename__ = "users"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(unique=True, index=True, max_length=255)
    name: str = Field(max_length=255)
    hashed_password: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to tasks
    tasks: list["Task"] = Relationship(back_populates="user")


class Task(SQLModel, table=True):
    """Task model for todo items."""
    __tablename__ = "tasks"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=255)
    description: Optional[str] = Field(default=None)
    completed: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to user
    user: Optional[User] = Relationship(back_populates="tasks")


# Pydantic models for API requests/responses
class UserCreate(SQLModel):
    """Schema for user registration."""
    email: str
    password: str
    name: str


class UserLogin(SQLModel):
    """Schema for user login."""
    email: str
    password: str


class UserResponse(SQLModel):
    """Schema for user response (no password)."""
    id: uuid.UUID
    email: str
    name: str
    created_at: datetime


class TokenResponse(SQLModel):
    """Schema for authentication token response."""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class TaskCreate(SQLModel):
    """Schema for task creation."""
    title: str
    description: Optional[str] = None


class TaskUpdate(SQLModel):
    """Schema for task update."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(SQLModel):
    """Schema for task response."""
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime
