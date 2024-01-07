from sanic import Blueprint, Request

bp = Blueprint("log", url_prefix="/log")


@bp.post("/")
def create_log(request: Request):
    pass
