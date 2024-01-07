from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column

from db.base import Info, Str250Type, Str60Type


@dataclass
class Tag(Info):
    name: Mapped[Str60Type] = mapped_column(comment="标签名")
    description: Mapped[Str250Type] = mapped_column(comment="标签描述")
