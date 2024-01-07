from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.comment.model import Comment
from app.group.model import Group
from app.post.model import Post
from app.user.table import user_group_table
from db.base import Info, Str250Type, Str60Type


@dataclass
class User(Info):
    username: Mapped[Str60Type] = mapped_column(comment="用户名")
    nickname: Mapped[Str60Type] = mapped_column(comment="用户昵称")
    description: Mapped[Str250Type] = mapped_column(comment="自我介绍")
    email: Mapped[Str250Type] = mapped_column(comment="Email")
    password: Mapped[Str250Type] = mapped_column(comment="密码")
    avatar: Mapped[Str250Type] = mapped_column(comment="头像URL")

    groups: Mapped[list[Group]] = relationship(secondary=user_group_table)
    posts: Mapped[list[Post]] = relationship()
    comments: Mapped[list[Comment]] = relationship()
