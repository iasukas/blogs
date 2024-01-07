from dataclasses import dataclass

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.category.model import Category
from app.comment.model import Comment
from app.post.table import post_category_table, post_tag_table, post_comment_table
from app.tag.model import Tag
from db.base import Info, Str250Type, Str60Type


@dataclass
class Post(Info):
    title: Mapped[Str60Type] = mapped_column(comment="文章标题")
    description: Mapped[Str250Type] = mapped_column(comment="文章描述")
    content: Mapped[str] = mapped_column(nullable=False, comment="文章正文")

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    categoies: Mapped[list[Category]] = relationship(secondary=post_category_table)
    tags: Mapped[list[Tag]] = relationship(secondary=post_tag_table)
    comments: Mapped[list[Comment]] = relationship(secondary=post_comment_table)
