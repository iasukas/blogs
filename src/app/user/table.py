from sqlalchemy import Table, Column, ForeignKey

from db.base import PrimaryKeyBase

user_group_table = Table(
    "user_group",
    PrimaryKeyBase.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("group_id", ForeignKey("group.id")),
)
