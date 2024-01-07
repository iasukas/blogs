from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from libs.schema import BaseSchema

type ModelType = Any
type CreateSchemaType = BaseSchema
type UpdateSchemaType = BaseSchema


class BaseInterface:
    model: ModelType

    def __init__(self, model: ModelType):
        self.model = model

    async def get(self, session: AsyncSession, model_id: int, *select_in_load_keys):
        async with session.begin():
            stmt = select(self.model).where(self.model.id == model_id).options(selectinload(*select_in_load_keys))
            result = await session.execute(stmt)
            data = result.scalar()
        return data.to_dict() if data else {}

    async def query_single(self, session: AsyncSession, *where_clause):
        async with session.begin():
            stmt = select(self.model).where(*where_clause).options(
                selectinload(self.model.relationship.selectin_load_fields)
            )
            result = await session.execute(stmt)
            data = result.scalar_one()
        return data.to_dict() if data else {}

    async def query(self, session: AsyncSession, *where_clause):
        async with session.begin():
            stmt = select(self.model).where(*where_clause).options(
                selectinload(self.model.relationship.selectin_load_fields)
            )
            result = await session.execute(stmt)
            data = result.scalars()
        return data if data else {}

    async def create(self, session: AsyncSession, data: Any):
        async with session.begin():
            model = self.model(**data)
            session.add(model)

    async def delete(self, session: AsyncSession, model_id: int):
        data = await self.get(session, model_id)
        if data:
            await session.delete(data)
            return data
        else:
            return None
