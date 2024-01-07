from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column

from db.base import Info, Str60Type


@dataclass
class Log(Info):
    ip: Mapped[Str60Type] = mapped_column(comment="客户端IP地址")
    user_agent: Mapped[str] = mapped_column(comment="客户端浏览器信息")
    method: Mapped[Str60Type] = mapped_column(comment="请求方法")
    uri: Mapped[str] = mapped_column(comment="请求URI")
    status_code: Mapped[int] = mapped_column(comment="请求状态码")
    time: Mapped[int] = mapped_column(comment="请求耗时（微秒）")
    request_headers: Mapped[str] = mapped_column(comment="请求头信息")
    request_body: Mapped[str] = mapped_column(comment="请求体信息")
    response_headers: Mapped[str] = mapped_column(comment="响应头信息")
    response_body: Mapped[str] = mapped_column(comment="响应体信息")
    exception_stack: Mapped[str] = mapped_column(comment="异常堆栈信息")
