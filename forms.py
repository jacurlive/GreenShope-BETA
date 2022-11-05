from fastapi import Form
from pydantic import BaseModel, validator
from bcrypt import hashpw, gensalt


class RegisterForm(BaseModel):
    username: str = Form()
    email: str = Form()
    password: str = Form()

    class Config:
        orm_mode = True

    @validator('password')
    def validate_password(cls, password):
        salt = gensalt()
        return hashpw(password.encode(), salt).decode()

    def is_valid(self):
        errors = []
        if len(self.email) < 4:
            errors.append('Check your email')
            return errors
        elif len(self.password) < 7:
            errors.append('Password must be more than 8')
            return errors
        return errors

    @classmethod
    def as_form(
            cls,
            username: str = Form(),
            email: str = Form(),
            password: str = Form()
    ):
        print(f'username: {username}\n'
              f'email: {email}\n'
              f'password: {password}')
        return cls(
            username=username,
            email=email,
            password=password
        )
