import re
from datetime import datetime
from typing import Literal, Annotated, get_args, Any

from sqlalchemy import func, BIGINT, TIMESTAMP, String, Enum, Text, JSON, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr, registry

Str60Type = Annotated[str, 60]
Str250Type = Annotated[str, 250]
TextType = Annotated[str, 999999]
StatusType = Literal["NORMAL", "PENDING", "BAN", "REMOVED"]


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            int: BIGINT,
            datetime: TIMESTAMP(timezone=True),
            Str60Type: String(60),
            Str250Type: String(250),
            str: Text(),
            dict[str, Any]: JSON,
            float: Float
        }
    )

    @classmethod
    @declared_attr.directive
    def __tablename__(cls):
        """
        将驼峰命名转换为下划线命名
        :return: 下划线命名
        """
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', cls.__name__).lower()


class PrimaryKeyBase(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Info(PrimaryKeyBase):
    __abstract__ = True

    status: Mapped[StatusType] = mapped_column(
        Enum(*get_args(StatusType), name="status_type", create_constraint=True, validate_strings=True),
        comment="数据状态"
    )
    create_datetime: Mapped[datetime] = mapped_column(server_default=func.now(), comment="创建时间")
    update_datetime: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        server_onupdate=func.now(),
        comment="更新时间"
    )
    remove_datetime: Mapped[datetime] = mapped_column(nullable=True, comment="删除时间")
