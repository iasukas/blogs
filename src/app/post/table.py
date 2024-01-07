from sqlalchemy import Table, Column, ForeignKey

from db.base import PrimaryKeyBase

post_category_table = Table(
    "post_category",
    PrimaryKeyBase.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("category_id", ForeignKey("category.id")),
)

post_comment_table = Table(
    "post_comment",
    PrimaryKeyBase.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("comment_id", ForeignKey("comment.id")),
)

post_tag_table = Table(
    "post_tag",
    PrimaryKeyBase.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("tag_id", ForeignKey("tag.id")),
)
