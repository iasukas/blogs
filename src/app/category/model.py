from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column

from db.base import Info, Str60Type, Str250Type


@dataclass
class Category(Info):
    parent_id: Mapped[int] = mapped_column(nullable=True, comment="父分类的ID")
    level: Mapped[int] = mapped_column(nullable=True, comment="分类层级")
    name: Mapped[Str60Type] = mapped_column(comment="分类名")
    description: Mapped[Str250Type] = mapped_column(comment="分类描述")
