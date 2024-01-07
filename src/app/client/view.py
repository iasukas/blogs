from dataclasses import dataclass

from authlib.jose import jwt
from mako.util import read_file
from sanic import Blueprint, Request, json
from sanic_ext import validate, serializer
from sanic_security.authentication import register
from sanic_security.verification import request_two_step_verification
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.user.model import User
from core.security import get_password_hash

bp = Blueprint("client", url_prefix="/client")


@dataclass
class SignInForm:
    account: str
    password: str
    private_pem_file: str


@bp.post("/signin/access-token")
@validate(form=SignInForm)
@serializer(json)
async def signin_access_token(request: Request, session: AsyncSession, form: SignInForm):
    header = {"alg": "RS256", "typ": "JWT"}
    password = get_password_hash(form.password)

    async with session.begin():
        stmt = select(User).where(
            or_(
                User.username == form.account,
                User.email == form.account
            ),
            User.password == password
        ).options(selectinload(User.groups))
        result = await session.execute(stmt)
        user = result.scalar()

    payload = {
        "iss": "Authlib",
        "sub": "123",
        "username": user.username,
        "email": user.email,
        "groups": user.groups,
    }
    private_key = read_file(form.private_pem_file)
    claims = jwt.encode(header, payload, private_key)

    return {"access_token": claims}


@bp.post("/password-recovery/{email}")
def recover_password_by_email(request: Request):
    pass


@bp.post("/reset-password")
def login_access_token(request: Request):
    pass


@bp.post("/signup/open")
@serializer(json)
async def signup_open(request: Request):
    account = await register(request)
    two_step_session = await request_two_step_verification(request, account)
    await email_code(account.email, two_step_session.code)

    response = json("Success", two_step_session.json)
    token = jwt.encode(response)
    return response


@bp.post("/signup/internal")
def signup_internal(request: Request):
    pass
