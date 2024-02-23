from fastapi import APIRouter
from Model.User import User, users

router = APIRouter()


@router.get("/users")
def get_users():
    return users


@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}


@router.post("/users")
def create_user(user: User):
    users.append(user)
    return user


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user.id == user_id:
            user.name = updated_user.name
            return user
    return {"error": "User not found"}


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"error": "User not found"}