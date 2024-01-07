from sqlalchemy import Table, Column, ForeignKey

from db.base import PrimaryKeyBase

group_permission_table = Table(
    "group_permission",
    PrimaryKeyBase.metadata,
    Column("group_id", ForeignKey("group.id")),
    Column("permission_id", ForeignKey("permission.id")),
)
