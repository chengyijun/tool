import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


# UserBase 作为模型的基础，其继承，相同的数据不要写 减少代码重复是FastAPI的核心思想之一
class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


class UserIn(UserBase):
    password: str


# 进行哈希密码
def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


# 保存用户
def fake_save_user(user_in: UserIn):
    hash_password = fake_password_hasher(user_in.password)
    # 保存用户
    # **user_id.dict() 表示一个完整的模型数据dict **称之为一个关键字参数
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hash_password)  # 伪哈希加密

    print("user saved! ... not really")

    print(user_in_db)

    return user_in_db


# response_model=UserOut 指定了序列化用到的类
@app.post("/user/", response_model=UserOut)  # 响应输入模型
async def create_user(*, user_in: UserIn):  # 响应输出模型
    user_saved = fake_save_user(user_in)
    return user_saved


if __name__ == "__main__":
    uvicorn.run(app)
