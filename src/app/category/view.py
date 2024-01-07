from sanic import Blueprint, Request, json
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.category.model import Category

bp = Blueprint("category", url_prefix="/category")


@bp.get("/")
async def read_categories(request: Request, session: AsyncSession):
    async with session.begin():
        stmt = select(Category).where(Category.id == 1)
        result = await session.execute(stmt)
        category = result.scalar()
        print(f"{category=}")

    if not category:
        return json({"code": 400, "msg": ""})

    return json({"code": 200, "msg": ""})


@bp.get("/{category_id}")
def read_category_by_id(request: Request):
    pass


@bp.post("/")
def create_category(request: Request):
    pass


@bp.put("/")
def update_category(request: Request):
    pass


@bp.delete("/{category_id}")
def delete_category_by_id(request: Request):
    pass
