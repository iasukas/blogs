from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.group.table import group_permission_table
from app.permission.model import Permission
from db.base import Info, Str250Type, Str60Type


@dataclass
class Group(Info):
    name: Mapped[Str60Type] = mapped_column(comment="分组名")
    description: Mapped[Str250Type] = mapped_column(comment="分组描述")

    permissions: Mapped[list[Permission]] = relationship(secondary=group_permission_table)
