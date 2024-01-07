from dataclasses import dataclass

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Info


@dataclass
class Comment(Info):
    content: Mapped[str] = mapped_column(nullable=False, comment="评论内容")
    likes: Mapped[int] = mapped_column(nullable=False, default=0, comment="点赞量")
    parent_id: Mapped[int] = mapped_column(nullable=True, comment="父评论的ID")
    level: Mapped[int] = mapped_column(nullable=True, comment="评论层级")

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
